import HW6


def calculate_markup_percent( t , n ):
    """ t = type & n = number """

    asghar = HW6.markup_list[int(t)-1]
    lower_cost = asghar['lower_cost']
    upper_cost = asghar['upper_cost']
    lower_count = asghar['lower_count']
    
    m = ( ( lower_cost - upper_cost ) / ( lower_count - 1 ) )
    soghra = ( m * (n-lower_count) ) + lower_cost
    akbar  = round( max( min( soghra , upper_cost ), lower_cost ), 3)

    return akbar

# print( calculate_markup_percent('1',5) )

def discount(product_type, userid, tota_price):
    
    commission_groups = HW6.product_list[int(product_type)-1]['commission_groups']

    asghar = list()
    [asghar.append([j['cost'], j['unit']]) for j in HW6.discount_list
        for i in commission_groups if (j['group_name'] == i and userid in j['users']) ]
    
    discount1 = list()
    [ discount1.append(i[0]*tota_price/100) if i[1] == 'percent' else discount1.append(i[0]) for i in asghar ]

    return max(discount1, default=0)



# def calculate_product_price( product_type, count, *userid ):
def calculate_product_price( product_type, count, userid=None ):
    
    asghar = dict()

    asghar['product_name'] = HW6.product_list[int(product_type)-1]['name']

    price = HW6.product_list[int(product_type)-1]['price']
    asghar['tota_price'] = count * (price + price * calculate_markup_percent(product_type,count)/100 )
    
    if userid and (userid in [ i['userid'] for i in HW6.user_list ]) :
        asghar['discount'] = discount(product_type, userid, asghar['tota_price'])
        asghar['username'] = HW6.user_list[userid-1001]
        del asghar['username']['userid']
    else:
        asghar['discount'] = 0
        asghar['username'] = {'first_name': '', 'last_name': ''}

    asghar['total_with_commission'] = asghar['tota_price'] - asghar['discount']

    return asghar

print(calculate_product_price("4",20,10005))





