from flask import Flask, render_template, request, redirect, \
					url_for, flash, jsonify
from conn import *

app = Flask(__name__)

# Making an API Endpoint (GET Request)
@app.route('/restaurants/<int:restaurant_id>/menu/JSON')

def restaurantMenuJSON(restaurant_id):
	#restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
	items = session.query(MenuItem).filter_by(restaurant_id = restaurant_id).all()
	return jsonify(MenuItems = [i.serialize for i in items])


@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON')

def specificMenuItem(restaurant_id, menu_id):
	specific_item = session.query(MenuItem).filter_by(id = menu_id).one()
	return jsonify(MenuItem = specific_item.serialize)

@app.route('/')
@app.route('/restaurants/<int:restaurant_id>')

def restaurantMenu(restaurant_id):
	restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
	items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)

	return render_template('menu.html', restaurant = restaurant, items = items)

@app.route("/restaurants/<int:restaurant_id>/new/", methods = ["GET", "POST"])
def newMenuItem(restaurant_id):
	if request.method == "POST":
		newItem = MenuItem(name = request.form['name'], \
							restaurant_id = restaurant_id)
		new_dish = newItem.name
		session.add(newItem)
		session.commit()

		flash("New item '%s' was created" % new_dish) 

		return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
	else:
		return render_template('newmenuitem.html', \
							restaurant_id = restaurant_id)

@app.route("/restaurants/<int:restaurant_id>/<int:menu_id>/edit/", methods = ["POST", "GET"])
def editMenuItem(restaurant_id, menu_id):
	item = session.query(MenuItem).filter_by(id = menu_id).one()

	if request.method == "POST":

		if request.form['new_name']:
			item.name = request.form['new_name']
			session.add(item)
			session.commit()

		flash("You successfully changed the name of item to '%s'" % item.name) 

		return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))

	else:
		return render_template('editmenu.html', restaurant_id = restaurant_id, \
								menu_id = menu_id, item_name = item.name)


@app.route("/restaurants/<int:restaurant_id>/<int:menu_id>/delete/", methods = ["POST", "GET"])
def deleteMenuItem(restaurant_id, menu_id):
	item = session.query(MenuItem).filter_by(id = menu_id).one()
	deleted_name = item.name

	if request.method == "POST":
		session.delete(item)
		session.commit()

		flash("You successfully deleted '%s'" % deleted_name)

		return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))

	else: 
		return render_template('deletemenuitem.html', item = item)


if __name__ == '__main__':
	app.secret_key = 'pashtet'
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)