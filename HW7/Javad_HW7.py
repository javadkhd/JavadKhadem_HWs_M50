import json
import HW6

class PMDU(): # P: product - M: markup - D: discount - U: user
    def __init__(self):
        self.products   = dict()
        self.markups    = dict()
        self.discoounts = dict()
        self.users      = dict()


    def add_product(self, type, name, price, unit, group):
        
        self.products.update({type: {"name":name, "price":price,\
            "unit":unit, "commission_groups":group}})


    def add_markup(self, product_type, lower_cost, upper_cost, unit, lower_count):
        
        self.markups.update({product_type: {"lower_cost":lower_cost,\
            "upper_cost":upper_cost, "unit":unit, "lower_count":lower_count}})


    def add_discount(self, group_name, cost, unit, users):
        
        self.discoounts.update({group_name: {"cost":cost, "unit":unit, "users":users}})


    def add_user(self, userid, first_name, last_name):
        
        self.users.update({userid: {"first_name":first_name, "last_name":last_name}})



class Shop():

    def __call__(self, name):

        self.name = name
    

    def markup(self, PMDU, product_type='0', count=1 ):

        if product_type in PMDU.markups.keys():
            lower_cost  = PMDU.markups[product_type]['lower_cost']
            upper_cost  = PMDU.markups[product_type]['upper_cost']
            lower_count = PMDU.markups[product_type]['lower_count']

            m = ( ( lower_cost - upper_cost ) / ( lower_count - 1 ) )
            line = ( m * (count-lower_count) ) + lower_cost
            sudo_satlin  = round( max( min( line , upper_cost ), lower_cost ), 3)

            return sudo_satlin
    

    def discount(self, PMDU, product_type, userid, tota_price):

        commission_groups = PMDU.products[product_type]["commission_groups"] if PMDU.products.get(product_type) else []
        
        discoounts = list()
        for group in commission_groups:
            if userid in PMDU.discoounts[group]["users"]:
                discoounts.append((PMDU.discoounts[group]["cost"], PMDU.discoounts[group]["unit"]))

        discount1 = list()
        [discount1.append(i[0]*tota_price/100) if i[1] == 'percent' else discount1.append(i[0]) for i in discoounts ]

        return max(discount1, default=0)
    

    def calculate_product_price(self, PMDU, product_type='0', count=1, userid=None):

        out = dict()
        price = PMDU.products.get(product_type).get("price") if PMDU.products.get(product_type) else 0

        out['tota_price'] = count * (price + price * self.markup(PMDU, product_type, count)/100 )\
            if self.markup(PMDU, product_type, count) else 0

        out['discount'] = self.discount(PMDU, product_type, userid, out['tota_price'])\
            if self.discount(PMDU, product_type, userid, out['tota_price']) else 0

        out['total_with_commission'] = out['tota_price'] - out['discount']
        out['product_name'] = PMDU.products[product_type]["name"] if PMDU.products.get(product_type) else None
        out['username'] = PMDU.users.get(userid)
        return out



def output(market=None, product_type=None, count=None, userid=None):

    print("\U0001F447 Invoice \U0001F447")
    print(f"Invoice = {json.dumps( market.calculate_product_price(pmdu, product_type, count, userid) , indent=4)}")
    print("\n\U0001F447 Markup \U0001F447")
    print(f"markup = {market.markup(pmdu, product_type, count)}")



if __name__ == "__main__":

    pmdu = PMDU()

    for product in HW6.product_list:
        pmdu.add_product(product['type'], product['name'], product['price'],\
            product['unit'], product['commission_groups'])
    # print(json.dumps(pmdu.products, indent=4))
    
    for markup in HW6.markup_list:
        pmdu.add_markup(markup['product_type'], markup['lower_cost'], markup['upper_cost'],\
            markup['unit'], markup['lower_count'])
    # print(json.dumps(pmdu.markups, indent=4))

    for discount in HW6.discount_list:
        pmdu.add_discount(discount['group_name'], discount['cost'],\
            discount['unit'], discount['users'])
    # print(json.dumps(pmdu.discoounts, indent=4))

    for user in HW6.user_list:
        pmdu.add_user(user['userid'], user['first_name'], user['last_name'])
    # print(json.dumps(pmdu.users, indent=4))


    minimarket = Shop()
    minimarket("SedEsmal")
    if hasattr(minimarket,'name'): print(minimarket.name)

    check_list = [
        ('product_type', 'count', 'userid'),
        (..., ..., ...),
        (),
        ('', '', ''),
        ('0', '0', '0'),
        (0, 0, 0),
        (0, 0,),
        ('ff', '0'),
        ('ff', ..., '00'),
        (..., '0', '00'),
        ('1', 10, 1005152),
        ('1', 5),
        ('2', 1),
        ('3', 20),
        ('1', 10, 1002),
        ('1', 15, 1003),
        ('2', 1),
        ]
    
    for elem in check_list:
        print(f"\n##############################\n{elem = }:\n")
        output(minimarket, *elem)

