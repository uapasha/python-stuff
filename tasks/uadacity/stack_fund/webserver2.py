from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi
from conn import session, Restaurant
from base_html import *

class webserverHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		try:
			output = header
			if self.path.endswith("/restaurants"):
				self.send_response(200)
				self.send_header("Content-type", "text/html")
				self.end_headers()


				restaurants = session.query(Restaurant).all()
				for i in restaurants:
					output += "<h2>"
					output += i.name
					output += "</h2><a href='restaurants/%s/edit'>Edit</a><br><a href='/%s/delete'>Delete</a>" % (i.id, i.id)

				output += "<a href = '/restaurants/new'><h2>Make a new Restaurant Here</h2></a>"	

			elif self.path.endswith("/restaurants/new"):
				self.send_response(200)
				self.send_header("Content-type", "text/html")
				self.end_headers()

				
				output += "<h2>Make a New Restaurant</h2>"

				form = """
					<form method = "POST" enctype = 'multipart/form-data' action = '/restaurants/new'>
						<input name = 'new_rest' type = 'text' placeholder = 'New Restaurant Name'>
						<input type = 'submit' value = 'Create'>
					</form>
				"""
				output += form

			elif self.path.endswith("/edit"):
				self.send_response(200)
				self.send_header("Content-type", "text/html")
				self.end_headers()

				rest_id = int(self.path.split("/")[-2])

				rename_restaurant = session.query(Restaurant).filter(Restaurant.id  == rest_id)
				

				output += "<h2>Rename the <strong>%s</strong></h2>"  % rename_restaurant[0].name

				form = """
					<form method = "POST" enctype = 'multipart/form-data' action = '/restaurants/%s/edit'>
						<input name = 'edit' type = 'text'>
						<input type = 'submit' value = 'Rename'>
					</form>
				""" % rest_id
				output += form


			elif self.path.endswith("/delete"):
				self.send_response(200)
				self.send_header("Content-type", "text/html")
				self.end_headers()



				rest_id = int(self.path.split("/")[-2])
				delete_restaurant = session.query(Restaurant).filter(Restaurant.id == rest_id)

				output += "<h2>You're going to delete Restaurant <strong>%s</strong>. Are you sure?</h2>" % delete_restaurant[0].name

				form = """
					<form method = "POST" enctype = 'multipart/form-data' action = '/delete'>
						<input name = 'delete_%s' type = 'submit' value = 'Delete'> </form>
				""" % rest_id

				output += form

			# add footer and write file
			output += footer
			self.wfile.write(output)
			return

		except IOError:
			self.send_error(404, 'File not found: %s', self.path)

	def do_POST(self):
		try:
			

			output = header
			
			ctype, pdict = cgi.parse_header(self.headers.getheader("content-type"))
			if ctype == 'multipart/form-data':
				fields = cgi.parse_multipart(self.rfile, pdict)

				restaurant = fields.get("new_rest")
				edit = fields.get("edit")

			if restaurant:
				self.send_response(301)
				self.end_headers()
				restaurant_new = Restaurant(name = restaurant[0])
				session.add(restaurant_new)
				session.commit()

				text = """
						<h2>New Restaurant was created!</h2>
						<p>Restaurant <strong>%s</strong> is added to restaurants</p>
						<a href = "/restaurants/new"><p>Back</p></a>
						<a href = "/restaurants"><p>To All restaurants</p></a>
 					""" % restaurant[0]

 				output += text
 				output += footer
				self.wfile.write(output)

 			elif edit:
 				self.send_response(301)
				self.end_headers()
 				rest_id = int(self.path.split("/")[-2])
 				new_name = edit[0]
 				old_rest = session.query(Restaurant).filter(Restaurant.id == rest_id)
 				old_name = old_rest[0].name
 				old_rest[0].name = new_name
 				session.add(old_rest[0])
 				session.commit()

 				text = """
 					<h2>You have changed the name of %s to %s.</h2>
 					<h3>Congrats!</h3>
					<a href = "/restaurants"><p>To All restaurants</p></a>
 				""" % (old_name, new_name)
 				output += text
 				output += footer
				self.wfile.write(output)

 			elif "delete" in fields.keys()[0]:
				del_command = fields.keys()[0]
				print "del del_command: ", del_command
				del_id = int(del_command.split("_")[1])
				delete_restaurant = session.query(Restaurant).filter(Restaurant.id == del_id).one()
				session.delete(delete_restaurant)
				session.commit()
				self.send_response(301)
				self.send_header('Content-type', 'text/html')
				self.send_header('Location', '/restaurants')
				self.end_headers()

		
		except Exception, e:
			print "ERROR! ", e
			pass

def main():
	try:
		port = 8080
		server = HTTPServer(("", port), webserverHandler)
		print "Web server is running on port %s" % port
		server.serve_forever()
	except KeyboardInterrupt:
		print "^C entered, web server is stoped"
		server.socket.close()

if __name__ == "__main__":
	main() 
