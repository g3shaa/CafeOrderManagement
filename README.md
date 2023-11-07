<h1>Cafe Order Management Documentation</h1>

<h2>Overview</h2>
<p>This Python program is a comprehensive solution for managing orders and menu items in a cafe. It provides a
    user-friendly interface for cafe staff to efficiently handle customer orders, track menu items, monitor table
    status, and print receipts. The system is designed to enhance the overall operation and customer service of a cafe.
</p>

<h2>Classes</h2>

<h3>MenuItem</h3>
<p>The <strong>MenuItem</strong> class represents an item on the cafe's menu. It consists of two essential attributes:
</p>
<ul>
    <li><strong>name</strong>: The name of the menu item.</li>
    <li><strong>price</strong>: The price of the menu item.</li>
</ul>

<h3>Order</h3>
<p>The <strong>Order</strong> class tracks individual customer orders. It includes the following attributes:</p>
<ul>
    <li><strong>table_number</strong>: The number of the table where the order was taken.</li>
    <li><strong>items</strong>: A list of menu items included in the order.</li>
</ul>

<h3>Cafe</h3>
<p>The <strong>Cafe</strong> class serves as the central component of the program, responsible for managing menu items,
    orders, table status, and order history.</p>
<p>It provides several crucial methods for the cafe's smooth operation:</p>
<ul>
    <li><strong>add_menu_item(name, price)</strong>: Adds a new menu item to the cafe's menu, enabling menu expansion.
    </li>
    <li><strong>take_order(table_number, items)</strong>: Records customer orders and updates table status to "Occupied"
        for the relevant table.</li>
    <li><strong>close_order(table_number)</strong>: Closes a customer's order, updates table status to "Vacant," records
        the order's total cost, and itemizes items in the order history.</li>
    <li><strong>load_data_from_json()</strong>: Loads essential data from a JSON file, including menu items, order
        history, and table status, ensuring data persistence.</li>
    <li><strong>save_data_to_json()</strong>: Saves data to a JSON file, including menu items, order history, and table
        status for future reference.</li>
</ul>

<h2>Functions</h2>

<h3>print_receipt(order, cafe)</h3>
<p>The <strong>print_receipt</strong> function generates a detailed receipt for a closed order. It calculates the total
    cost and provides an itemized list of items in the order. This function facilitates transparency and professionalism
    in customer service.</p>

<h2>Usage</h2>
<p>The program is designed for easy and intuitive use by cafe staff. The <strong>main()</strong> function is the entry
    point, offering a console-based interface for users to interact with the cafe order management system. Staff members
    can perform various tasks:</p>
<ul>
    <li>Add menu items to the cafe's menu, including item names and prices.</li>
    <li>Take orders for specific tables, selecting items from the menu.</li>
    <li>Close orders, which calculates the total cost, updates table status, and archives the order in the history.</li>
    <li>View the current menu, displaying all available menu items and their prices.</li>
    <li>Check the table status, showing whether each table is occupied or vacant.</li>
    <li>Print receipts for closed orders, ensuring accuracy and professionalism in customer service.</li>
    <li>Exit the program, completing the workflow.</li>
</ul>

<h2>Data Persistence</h2>
<p>The program automatically loads data from a JSON file upon startup. This includes the cafe's menu items, order
    history, and table status. When the program exits, it saves this data to the same JSON file, ensuring that all
    information is persistently stored for future use.</p>

<h2>Conclusion</h2>
<p>The Cafe Order Management program is a versatile and efficient tool for cafe operations. By managing orders, tracking
    menu items, and providing table status information, it empowers cafe staff to offer top-quality service to
    customers. Data persistence ensures that important information is retained across program restarts, allowing the
    cafe to maintain a consistent and professional operation.</p>
