
temp = ['Hot', 'Iced']

hot_syrup = ['Brown Sugar', 'Cinnamon Dolce', 'Vanilla', 'Caramel', 'Hazelnut', 'Toffee Nut', 'Honey Blend'
             , 'White Chocolate']
hot_brew = ['Pike Place', 'Blonde Roast', 'Dark Roast', ]
hot_coffee = ['Americano', 'Caffe Misto', 'Cappuccino'
            , 'Espresso Con Panna', 'Flat White', 'Latte', 'Macchiato', 'Mocha', 'Espresso']
hot_other = ['Hot Chocolate', 'White Hot Chocolate', 'Caramel Apple Spice', 'Peppermint Hot Chocolate'
             , 'Vanilla Creme']
hot_tea = ['Chai Tea Latte', 'Chai Tea', 'Earl Grey', 'London Fog Tea Latte', 'Royal English Breakfast Tea Latte'
           ,'Royal English Breakfast Tea', 'Matcha Tea Latte', 'Honey Citrus Mint Tea', 'Jade Citrus Mint Tea'
           ,'Mint Majesty Tea', 'Peach Tranquility Tea', 'Emeperor\'s Clouds and Mist Tea']
hot_drink = [hot_coffee, hot_other, hot_tea, hot_brew]
hot_caf = [hot_coffee, hot_tea, hot_brew]
hot_decaf = [["Decaf " + s for s in hot_coffee] ,hot_other, ["Decaf " + s for s in hot_brew]]

frappuccino_c = ['Mocha Cookie Crumble Frappuccino', 'Caramel Ribbon Crunch Frappuccino', 'Espresso Frappucchino'
               , 'Caffe Vanilla Frappucchino', 'Caramel Frappuccino', 'Coffee Frappucchino', 'Mocha Frappucchino'
               , 'Java Chip Frappucchino', 'White Chocolate Mocha Frappuccino']
frappuccino_d = ['Chocolate Cookie Crumble Creme Frappuccino', 'Caramel Ribbon Crunch Creme Frappuccino'
               , 'Strawberry Creme Frappuccino', 'Chai Creme Frappuccino', 'Double Chocolaty Chip Creme Frappuccino'
               , 'Matcha Creme Frappuccino', 'Vanilla Bean Creme Frappuccino', 'White Chocolate Creme Frappuccino']
cold_brew = ['Cinnamon Caramel Cream Cold Brew', 'Chocolate Cream Cold Brew', 'Salted Caramel Cream Cold Brew'
             , 'Cold Brew', 'Vanilla Sweet Cream Cold Brew', 'Cold Brew with Milk', 'Cinnamon Caramel Nitro Cold Brew'
             , 'Nitro Cold Brew', 'Vanilla Sweet Cream Nitro Cold Brew']
shaken = ['Iced Toasted Vanilla Shaken Espresso', 'Iced Brown Sugar Shaken Espresso', 'Iced Chocolate Shaken Espresso'
          , 'Iced Shaken Espresso']
refresher = ['Dragon Drink Refresher', 'Mango Dragonfruit Refresher', 'Paradise Drink Refresher'
             , 'Strawberry Acai Refresher', 'Pineapple Passionfruit Refresher', 'Pink Drink Refresher']
iced_tea = ['Iced Black Tea', 'Iced Green Tea']
iced_syrup = ['Lemonade', 'Green Tea Base', 'Passion Tango Tea Base', 'Green Tea Base', 'Peach']

iced_drink = [frappuccino_c, frappuccino_d, ["Iced " + s for s in hot_coffee], cold_brew, shaken, iced_tea, refresher
              , ["Iced " + s for s in hot_tea]]
iced_caf = [frappuccino_c, refresher, iced_tea, ["Iced " + s for s in hot_tea]]
iced_decaf = [frappuccino_d, ['Passion Tango Tea']]