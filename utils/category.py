from oscar.apps.catalogue.categories import create_from_breadcrumbs

# menu =  ['Shoes', 'Casual Shoes', 'Formal Shoes', 'Loafers', 'Half Loafer', 'Tassel Shoes & Penny Loafers', 'Nagras Shoes', 'Men’s Sandal', 'Elegance', 'Women’s Sandals', 'Ladies Heel', 'Ladies Sports Shoes', 'Bags', 'Backpacks', 'Crossbody Bag', 'Executive Bags', 'Laptop Bags', 'Messenger Bags', 'Travel Bags', 'Hand Bags', 'Saddle Bag', 'Tote Bags', 'Wallet', 'Card Holder', 'Leather Pouch', 'Long Wallet', 'Passport Holder', 'Short Wallet', 'Zip Wallet', 'Belt', 'Buckle', 'Accessories', 'ID Card Holder', 'Key Ring', 'Leather Mouse Pad', 'Insole', 'Campaigns', 'Blog', 'Shoes', 'Casual Shoes', 'Formal Shoes', 'Loafers', 'Half Loafer', 'Tassel Shoes & Penny Loafers', 'Nagras Shoes', 'Men’s Sandal', 'Elegance', 'Women’s Sandals', 'Ladies Heel', 'Ladies Sports Shoes', 'Bags', 'Backpacks', 'Crossbody Bag', 'Executive Bags', 'Laptop Bags', 'Messenger Bags', 'Travel Bags', 'Hand Bags', 'Saddle Bag', 'Tote Bags', 'Wallet', 'Card Holder', 'Leather Pouch', 'Long Wallet', 'Passport Holder', 'Short Wallet', 'Zip Wallet', 'Belt', 'Buckle', 'Accessories', 'ID Card Holder', 'Key Ring', 'Leather Mouse Pad', 'Insole', 'Campaigns', 'Blog', 'Shoes']
categories = (
    "Shoes > Man's Shoes > Casual Shoes",
    "Shoes > Man's Shoes > Formal Shoes",
    "Shoes > Man's Shoes > Half Loafer",
    "Shoes > Man's Shoes > Tassel Shoes & Penny Loafers",
    "Shoes > Man's Shoes > Nagras Shoes",
    "Shoes > Man's Shoes > Men’s Sandal",
    "Shoes > Man's Shoes > Ladies Heel",
    "Shoes > Women's Shoes > Women’s Sandals",
    "Shoes > Women's Shoes > Ladies Sports Shoes",
    "Begs > Man's Beg > Backpacks",
    "Begs > Man's Beg > Crossbody Bag",
    "Begs > Man's Beg > Executive Bags",
    "Begs > Man's Beg > Laptop Bags",
    "Begs > Man's Beg > Messenger  Bags",
    "Begs > Man's Beg > Travel  Bags",
    "Begs > Women's Beg > Hand  Bags",
    "Begs > Women's Beg > Saddle  Bags",
    "Begs > Women's Beg > Tote  Bags",
    "Wallet > Men's Wallet & Purse > Card Holder",
    "Wallet > Men's Wallet & Purse > Leather Pouch",
    "Wallet > Men's Wallet & Purse > Long Wallet",
    "Wallet > Men's Wallet & Purse > Short Wallet",
    "Wallet > Men's Wallet & Purse > Zip Wallet",
    "Wallet > Women's Wallet & Purse ",
    "Belt > Buckle",
    "Accessories > Meat",
    "Accessories > ID Card Holder",
    "Accessories > Key Ring",
    "Accessories >Leather Mouse Pad",
    "Accessories >Insole",
)
for breadcrumbs in categories:
    create_from_breadcrumbs(breadcrumbs)
