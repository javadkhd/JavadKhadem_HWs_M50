import json
import HW6


class Product():

    def __init__(self):
        self.product_list = dict()

    def add_product(self, type, name, price, unit, group):
        
        self.product_list.update({type: {"name":name, "price":price,\
             "unit":unit, "commission_groups":group}})


class Markup():

    def __init__(self):
        self.markup_list = dict()

    def add_markup(self, product_type, lower_cost, upper_cost, unit, lower_count):
        
        self.markup_list.update({product_type: {"lower_cost":lower_cost,\
            "upper_cost":upper_cost, "unit":unit, "lower_count":lower_count}})



class Discount():

    def __init__(self):
        self.discount_list = dict()

    def add_discount(self, group_name, cost, unit, users):
        
        self.discount_list.update({group_name: {"cost":cost, "unit":unit, "users":users}})


class User():

    def __init__(self):
        self.user_list = dict()

    def add_user(self, userid, first_name, last_name):
        
        self.user_list.update({userid: {"first_name":first_name, "last_name":last_name}})



class Shop():

    def __call__(self, name):
        self.name = name
    

    def markup(self, Markup, product_type='0', count=1 ):
        if product_type in Markup.markup_list.keys():
            lower_cost  = Markup.markup_list[product_type]['lower_cost']
            upper_cost  = Markup.markup_list[product_type]['upper_cost']
            lower_count = Markup.markup_list[product_type]['lower_count']

            m = ( ( lower_cost - upper_cost ) / ( lower_count - 1 ) )
            line = ( m * (count-lower_count) ) + lower_cost
            sudo_satlin  = round( max( min( line , upper_cost ), lower_cost ), 3)

            return sudo_satlin
    

    def discount(self, Product, Discount, product_type, userid, tota_price):

        commission_groups = Product.product_list[product_type]["commission_groups"] if Product.product_list.get(product_type) else []
        
        discount_list = list()
        for group in commission_groups:
            if userid in Discount.discount_list[group]["users"]:
                discount_list.append((Discount.discount_list[group]["cost"], Discount.discount_list[group]["unit"]))

        discount1 = list()
        [discount1.append(i[0]*tota_price/100) if i[1] == 'percent' else discount1.append(i[0]) for i in discount_list ]

        return max(discount1, default=0)
    

    def calculate_product_price(self, Product, Discount, Markup, User, product_type='0', count=1, userid=None):

        out = dict()
        price = Product.product_list.get(product_type).get("price") if Product.product_list.get(product_type) else 0

        out['tota_price'] = count * (price + price * self.markup(Markup, product_type, count)/100 ) if self.markup(Markup, product_type, count) else 0
        out['discount'] = self.discount(Product, Discount, product_type, userid, out['tota_price']) if self.discount(Product, Discount, product_type, userid, out['tota_price']) else 0
        out['total_with_commission'] = out['tota_price'] - out['discount']
        out['product_name'] = Product.product_list[product_type]["name"] if Product.product_list.get(product_type) else None
        out['username'] = User.user_list.get(userid)
        return out



def output(market=None, product_type=None, count=None, userid=None):
    print("\U0001F447 Invoice \U0001F447")
    print(f"Invoice = {json.dumps( market.calculate_product_price(products, discounts, markups, users, product_type, count, userid) , indent=4)}")
    print("\n\U0001F447 Markup \U0001F447")
    print(f"markup = {market.markup(markups, product_type, count)}")



if __name__ == "__main__":

    products = Product()
    for product in HW6.product_list:
        products.add_product(product['type'], product['name'], product['price'],\
            product['unit'], product['commission_groups'])
    # print(json.dumps(products.product_list, indent=4))
    # print("##############################\n##############################")
    
    markups = Markup()
    for markup in HW6.markup_list:
        markups.add_markup(markup['product_type'], markup['lower_cost'], markup['upper_cost'],\
            markup['unit'], markup['lower_count'])
    # print(json.dumps(markups.markup_list, indent=4))
    # print("##############################\n##############################")

    discounts = Discount()
    for discount in HW6.discount_list:
        discounts.add_discount(discount['group_name'], discount['cost'],\
            discount['unit'], discount['users'])
    # print(json.dumps(discounts.discount_list, indent=4))
    # print("##############################\n##############################")

    users = User()
    for user in HW6.user_list:
        users.add_user(user['userid'], user['first_name'], user['last_name'])
    # print(json.dumps(users.user_list, indent=4))
    # print("##############################\n##############################")


    minimarket = Shop()
    minimarket("SedEsmal")
    if hasattr(minimarket,'name'): print(minimarket.name)
    # print(aa)

    check_list = [
        ('product_type', 'count', 'userid'),
        ('', '', ''),
        ('0', '0', '0'),
        (0, 0, 0),
        ('ff', '0',...),
        ('ff', ..., '00'),
        (..., '0', '00'),
        ('1', 10, 1005152),
        ('1', 5, ...),
        ('2', 1, ...),
        ('3', 20, ...),
        ('1', 10, 1002),
        ('1', 15, 1003),
        ('2', 1, ...),
        ]
    
    for elem in check_list:
        print(f"\n##############################\n{elem = }")
        output(minimarket, elem[0], elem[1], elem[2])









