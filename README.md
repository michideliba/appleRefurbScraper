# appleRefurbScraper

This code is scraper for Apple refurbished HP.

# Dependency

```shell
Python 3.8.10
requests 2.22.0
beautifulsoup4 4.10.0
```

# Install and run the app

```shell
$ python3 -m pip install requests
$ python3 -m pip install beautifulsoup4
$ python3 appleRefurbScraper.py
```

# Input

Setting parameters are below.

|name|ex|
|:---|:---|
|domain   |'https://www.apple.com/shop/refurbished/'|
|scrapList|['mac', 'ipad', 'iphone', 'watch', 'ipod', 'appletv', 'clearance', 'accessories']|
|listClass|'rf-refurb-category-grid-no-js' or 'refurbished-category-grid-no-js'|
|listTag  |'li'|
|nameTag  |'a'|
|priceTag |'div'|

The above parameters assume the following tag structure.

```shell
  <div class="rf-refurb-category-grid-no-js">
    <li>
      <a href="">name</a>
      <div>price</div>
    </li><li>
      ...
```

# Output

Print item name and price(The below is example in July 04, 2022) and save HP data.

```shell
$ python3 appleRefurbScraper.py 
start scraper!
mac
[['Refurbished Mac mini Apple M1 Chip with 8‑Core CPU and 8‑Core GPU', '$589.00'],
 ['Refurbished Mac mini 3.6GHz quad-core Intel Core i3 - Space Gray', '$679.00'],
 ['Refurbished Mac mini Apple M1 Chip with 8‑Core CPU and 8‑Core GPU', '$759.00'],
 ['Refurbished Mac mini 3.0GHz 6-core Intel Core i5 - Space Gray', '$759.00'],
 ['Refurbished 13.3-inch MacBook Air Apple M1 Chip with 8‑Core CPU and 7‑Core GPU - Gold', '$849.00'],
 ['Refurbished 13.3-inch MacBook Air Apple M1 Chip with 8‑Core CPU and 7‑Core GPU - Silver', '$849.00'],
 ['Refurbished 13.3-inch MacBook Air Apple M1 Chip with 8‑Core CPU and 7‑Core GPU - Space Gray', '$849.00'],
 ['Refurbished 21.5-inch iMac 2.3GHz dual-core Intel Core i5', '$889.00'],
 ['Refurbished 21.5-inch iMac 3.6GHz quad-core Intel Core i3 with Retina 4K display', '$899.00'],
 ['Refurbished Mac mini Apple M1 Chip with 8‑Core CPU and 8‑Core GPU', '$929.00'],
 ['Refurbished 21.5-inch iMac 2.3GHz dual-core Intel Core i5', '$929.00'],
 ['Refurbished Mac mini Apple M1 Chip with 8‑Core CPU and 8‑Core GPU', '$929.00'],
 ['Refurbished 21.5-inch iMac 2.3GHz dual-core Intel Core i5', '$929.00'],
 ['Refurbished Mac mini 3.0GHz 6-core Intel Core i5 - Space Gray', '$929.00'],
 ['Refurbished 13.3-inch MacBook Pro Apple M1 Chip with 8‑Core CPU and 8‑Core GPU - Space Gray', '$1,059.00'],
 ['Refurbished 13.3-inch MacBook Air Apple M1 Chip with 8‑Core CPU and 8‑Core GPU - Silver', '$1,059.00'],
 ['Refurbished 13.3-inch MacBook Air Apple M1 Chip with 8‑Core CPU and 8‑Core GPU - Space Gray', '$1,059.00'],
 ['Refurbished 21.5-inch iMac 2.3GHz dual-core Intel Core i5', '$1,059.00'],
 ['Refurbished 13.3-inch MacBook Pro Apple M1 Chip with 8‑Core CPU and 8‑Core GPU - Silver', '$1,059.00'],
 ['Refurbished 13.3-inch MacBook Air Apple M1 Chip with 8‑Core CPU and 8‑Core GPU - Gold', '$1,059.00'],
 ['Refurbished Mac mini Apple M1 Chip with 8‑Core CPU and 8‑Core GPU', '$1,099.00'],
 ['Refurbished 21.5-inch iMac 3.6GHz quad-core Intel Core i3 with Retina 4K display', '$1,099.00'],
 ['Refurbished 21.5-inch iMac 2.3GHz dual-core Intel Core i5', '$1,099.00'],
 ['Refurbished Mac mini 3.2GHz 6-core Intel Core i7 - Space Gray', '$1,099.00'],
 ['Refurbished Mac mini 3.0GHz 6-core Intel Core i5 - Space Gray', '$1,099.00'],
 ['Refurbished 21.5-inch iMac 2.3GHz dual-core Intel Core i5', '$1,099.00'],
 ['Refurbished 21.5-inch iMac 3.6GHz quad-core Intel Core i3 with Retina 4K display', '$1,099.00'],
 ['Refurbished Mac mini Apple M1 Chip with 8‑Core CPU and 8‑Core GPU, 10GB Ethernet', '$1,189.00'],
 ['Refurbished 13.3-inch MacBook Pro Apple M1 Chip with 8‑Core CPU and 8‑Core GPU - Silver', '$1,229.00'],
 ['Refurbished 13.3-inch MacBook Pro Apple M1 Chip with 8‑Core CPU and 8‑Core GPU - Space Gray', '$1,229.00'],
 ['Refurbished 21.5-inch iMac 3.6GHz quad-core Intel Core i3 with Retina 4K display', '$1,269.00'],
 ['Refurbished Mac mini 3.0GHz 6-core Intel Core i5 - Space Gray', '$1,269.00'],
 ['Refurbished 21.5-inch iMac 3.0GHz 6-core Intel Core i5 with Retina 4K display', '$1,269.00'],
 ['Refurbished Mac mini Apple M1 Chip with 8‑Core CPU and 8‑Core GPU', '$1,269.00'],
 ['Refurbished 13.3-inch MacBook Air Apple M1 Chip with 8‑Core CPU and 8‑Core GPU - Space Gray', '$1,399.00'],
 ['Refurbished 13.3-inch MacBook Air Apple M1 Chip with 8‑Core CPU and 8‑Core GPU - Gold', '$1,399.00'],
 ['Refurbished 24-inch iMac Apple M1 Chip with 8‑Core CPU and 8‑Core GPU, Gigabit Ethernet - Pink', '$1,439.00'],
 ['Refurbished 21.5-inch iMac 3.2GHz 6-core Intel Core i7 with Retina 4K display', '$1,439.00'],
 ['Refurbished 21.5-inch iMac 3.6GHz quad-core Intel Core i3 with Retina 4K display', '$1,439.00'],
 ['Refurbished Mac mini 3.2GHz 6-core Intel Core i7 - Space Gray', '$1,439.00'],
 ['Refurbished 21.5-inch iMac 3.2GHz 6-core Intel Core i7 with Retina 4K display', '$1,439.00'],
 ['Refurbished Mac mini 3.0GHz 6-core Intel Core i5 - Space Gray', '$1,439.00'],
 ['Refurbished 21.5-inch iMac 3.0GHz 6-core Intel Core i5 with Retina 4K display', '$1,439.00'],
 ['Refurbished 21.5-inch iMac 3.0GHz 6-core Intel Core i5 with Retina 4K display', '$1,439.00'],
 ['Refurbished Mac mini Apple M1 Chip with 8‑Core CPU and 8‑Core GPU', '$1,439.00'],
 ['Refurbished 24-inch iMac Apple M1 Chip with 8‑Core CPU and 8‑Core GPU, Gigabit Ethernet - Green', '$1,439.00'],
 ['Refurbished 21.5-inch iMac 3.0GHz 6-core Intel Core i5 with Retina 4K display', '$1,439.00'],
 ['Refurbished 24-inch iMac Apple M1 Chip with 8‑Core CPU and 8‑Core GPU, Gigabit Ethernet - Orange', '$1,439.00'],
 ['Refurbished Mac mini Apple M1 Chip with 8‑Core CPU and 8‑Core GPU, 10GB Ethernet', '$1,529.00'],
 ['Refurbished 21.5-inch iMac 3.0GHz 6-core Intel Core i5 with Retina 4K display and Radeon Pro Vega 20', '$1,569.00'],
 ['Refurbished 21.5-inch iMac 3.0GHz 6-core Intel Core i5 with Retina 4K display and Radeon Pro Vega 20', '$1,569.00'],
 ['Refurbished 21.5-inch iMac 3.0GHz 6-core Intel Core i5 with Retina 4K display', '$1,609.00'],
 ['Refurbished Mac mini 3.2GHz 6-core Intel Core i7 - Space Gray', '$1,609.00'],
 ['Refurbished 21.5-inch iMac 3.6GHz quad-core Intel Core i3 with Retina 4K display', '$1,609.00'],
 ['Refurbished 21.5-inch iMac 3.0GHz 6-core Intel Core i5 with Retina 4K display', '$1,609.00'],
 ['Refurbished 21.5-inch iMac 3.2GHz 6-core Intel Core i7 with Retina 4K display', '$1,609.00'],
 ['Refurbished 21.5-inch iMac 3.2GHz 6-core Intel Core i7 with Retina 4K display', '$1,609.00'],
 ['Refurbished 21.5-inch iMac 3.2GHz 6-core Intel Core i7 with Retina 4K display', '$1,609.00'],
 ['Refurbished 21.5-inch iMac 3.2GHz 6-core Intel Core i7 with Retina 4K display and Radeon Pro Vega 20', '$1,739.00'],
 ['Refurbished Mac mini 3.2GHz 6-core Intel Core i7 - Space Gray', '$1,779.00'],
 ['Refurbished 27-inch iMac 3.0GHz 6-core Intel Core i5 with Retina 5K display', '$1,779.00'],
 ['Refurbished 21.5-inch iMac 3.0GHz 6-core Intel Core i5 with Retina 4K display', '$1,779.00'],
 ['Refurbished 27-inch iMac 3.1GHz 6-core Intel Core i5 with Retina 5K display', '$1,869.00'],
 ['Refurbished 21.5-inch iMac 3.0GHz 6-core Intel Core i5 with Retina 4K display and Radeon Pro Vega 20', '$1,909.00'],
 ['Refurbished 21.5-inch iMac 3.0GHz 6-core Intel Core i5 with Retina 4K display and Radeon Pro Vega 20', '$1,909.00'],
 ['Refurbished 21.5-inch iMac 3.2GHz 6-core Intel Core i7 with Retina 4K display and Radeon Pro Vega 20', '$1,909.00'],
 ['Refurbished 21.5-inch iMac 3.2GHz 6-core Intel Core i7 with Retina 4K display', '$1,949.00'],
 ['Refurbished Mac mini 3.2GHz 6-core Intel Core i7 - Space Gray', '$2,119.00'],
 ['Refurbished Mac mini 3.2GHz 6-core Intel Core i7 - Space Gray', '$2,209.00'],
 ['Refurbished 21.5-inch iMac 3.2GHz 6-core Intel Core i7 with Retina 4K display and Radeon Pro Vega 20', '$2,249.00'],
 ['Refurbished 21.5-inch iMac 3.2GHz 6-core Intel Core i7 with Retina 4K display', '$2,289.00'],
 ['Refurbished Mac mini 3.2GHz 6-core Intel Core i7 - Space Gray', '$2,459.00'],
 ['Refurbished Mac mini 3.2GHz 6-core Intel Core i7, 10GB Ethernet - Space Gray', '$2,549.00'],
 ['Refurbished 21.5-inch iMac 3.2GHz 6-core Intel Core i7 with Retina 4K display and Radeon Pro Vega 20', '$2,589.00'],
 ['Refurbished 27-inch iMac 3.1GHz 6-core Intel Core i5 with Retina 5K display', '$3,179.00'],
 ['Refurbished 27-inch iMac 3.1GHz 6-core Intel Core i5 with Retina 5K display, 10GB Ethernet', '$3,249.00'],
 ['Refurbished 27-inch iMac Pro 3.2GHz 8-core Intel Xeon W with Retina 5K display', '$3,249.00'],
 ['Refurbished 27-inch iMac 3.8GHz 8-core Intel Core i7 with Retina 5K display, 10GB Ethernet', '$3,679.00'],
 ['Refurbished 27-inch iMac 3.6GHz 10-core Intel Core i9 with Retina 5K display, 10GB Ethernet', '$3,759.00'],
 ['Refurbished 27-inch iMac Pro 3.2GHz 8-core Intel Xeon W with Retina 5K display', '$4,159.00'],
 ['Refurbished 27-inch iMac 3.6GHz 10-core Intel Core i9 with Retina 5K display', '$4,189.00'],
 ['Refurbished 27-inch iMac Pro 3.0GHz 10-core Intel Xeon W with Retina 5K display', '$4,249.00'],
 ['Refurbished 27-inch iMac Pro 3.2GHz 8-core Intel Xeon W with Retina 5K display', '$4,289.00'],
 ['Refurbished 27-inch iMac 3.6GHz 10-core Intel Core i9 with Retina 5K display', '$4,329.00'],
 ['Refurbished 27-inch iMac 3.8GHz 8-core Intel Core i7 with Retina 5K display', '$4,329.00'],
 ['Refurbished 27-inch iMac 3.6GHz 10-core Intel Core i9 with Retina 5K display', '$4,479.00'],
 ['Refurbished 27-inch iMac 3.6GHz 10-core Intel Core i9 with Retina 5K display, Nano-texture glass', '$4,479.00'],
 ['Refurbished 27-inch iMac Pro 3.0GHz 10-core Intel Xeon W with Retina 5K display', '$4,589.00'],
 ['Refurbished 27-inch iMac Pro 3.0GHz 10-core Intel Xeon W with Retina 5K display', '$4,589.00'],
 ['Refurbished 27-inch iMac 3.6GHz 10-core Intel Core i9 with Retina 5K display', '$4,619.00'],
 ['Refurbished 27-inch iMac Pro 3.2GHz 8-core Intel Xeon W with Retina 5K display', '$4,629.00'],
 ['Refurbished 27-inch iMac Pro 3.0GHz 10-core Intel Xeon W with Retina 5K display', '$4,719.00'],
 ['Refurbished 27-inch iMac Pro 3.0GHz 10-core Intel Xeon W with Retina 5K display', '$4,929.00'],
 ['Refurbished 27-inch iMac Pro 2.5GHz 14-core Intel Xeon W with Retina 5K display', '$4,929.00'],
 ['Refurbished 27-inch iMac Pro 3.0GHz 10-core Intel Xeon W with Retina 5K display', '$5,059.00'],
 ['Refurbished 27-inch iMac Pro 3.0GHz 10-core Intel Xeon W with Retina 5K display', '$5,059.00'],
 ['Refurbished 27-inch iMac Pro 3.0GHz 10-core Intel Xeon W with Retina 5K display', '$5,099.00'],
 ['Refurbished 27-inch iMac Pro 3.0GHz 10-core Intel Xeon W with Retina 5K display and Radeon Pro Vega 64X', '$5,179.00'],
 ['Refurbished Mac Pro 3.5GHz 8-core Intel Xeon W, Radeon Pro 580X', '$5,179.00'],
 ['Refurbished 27-inch iMac Pro 2.5GHz 14-core Intel Xeon W with Retina 5K display', '$5,269.00'],
 ['Refurbished 27-inch iMac Pro 2.5GHz 14-core Intel Xeon W with Retina 5K display', '$5,269.00'],
 ['Refurbished 27-inch iMac Pro 2.5GHz 14-core Intel Xeon W with Retina 5K display', '$5,399.00'],
 ['Refurbished 27-inch iMac Pro 3.0GHz 10-core Intel Xeon W with Retina 5K display', '$5,399.00'],
 ['Refurbished 27-inch iMac Pro 3.0GHz 10-core Intel Xeon W with Retina 5K display', '$5,439.00'],
 ['Refurbished 27-inch iMac Pro 2.5GHz 14-core Intel Xeon W with Retina 5K display', '$5,609.00'],
 ['Refurbished Mac Pro 3.5GHz 8-core Intel Xeon W, Radeon Pro 580X', '$5,609.00'],
 ['Refurbished 27-inch iMac Pro 2.5GHz 14-core Intel Xeon W with Retina 5K display', '$5,739.00'],
 ['Refurbished 27-inch iMac Pro 3.0GHz 10-core Intel Xeon W with Retina 5K display', '$5,909.00'],
 ['Refurbished 27-inch iMac Pro 2.3GHz 18-core Intel Xeon W with Retina 5K display', '$5,949.00'],
 ['Refurbished Mac Pro 3.5GHz 8-core Intel Xeon W, Radeon Pro W5700X', '$6,029.00'],
 ['Refurbished 27-inch iMac Pro 2.5GHz 14-core Intel Xeon W with Retina 5K display', '$6,079.00'],
 ['Refurbished Mac Pro 3.5GHz 8-core Intel Xeon W, Radeon Pro 580X', '$6,289.00'],
 ['Refurbished 27-inch iMac Pro 3.0GHz 10-core Intel Xeon W with Retina 5K display', '$6,289.00'],
 ['Refurbished 27-inch iMac Pro 2.3GHz 18-core Intel Xeon W with Retina 5K display', '$6,289.00'],
 ['Refurbished 27-inch iMac Pro 2.3GHz 18-core Intel Xeon W with Retina 5K display', '$6,419.00'],
 ['Refurbished Mac Pro 3.5GHz 8-core Intel Xeon W, Radeon Pro 580X', '$6,459.00'],
 ['Refurbished 27-inch iMac Pro 3.0GHz 10-core Intel Xeon W with Retina 5K display', '$6,759.00'],
 ['Refurbished 27-inch iMac Pro 2.3GHz 18-core Intel Xeon W with Retina 5K display and Radeon Pro Vega 64X', '$6,879.00'],
 ['Refurbished 27-inch iMac Pro 2.3GHz 18-core Intel Xeon W with Retina 5K display', '$7,309.00'],
 ['Refurbished Mac Pro 3.3GHz 12-core Intel Xeon W, Radeon Pro 580X', '$7,389.00'],
 ['Refurbished Mac Pro 3.3GHz 12-core Intel Xeon W, Radeon Pro W5700X', '$7,479.00'],
 ['Refurbished 27-inch iMac Pro 2.3GHz 18-core Intel Xeon W with Retina 5K display and Radeon Pro Vega 64X', '$7,899.00'],
 ['Refurbished Mac Pro 3.2GHz 16-core Intel Xeon W, Radeon Pro 580X', '$7,989.00'],
 ['Refurbished 27-inch iMac Pro 2.5GHz 14-core Intel Xeon W with Retina 5K display and Radeon Pro Vega 64X', '$8,069.00'],
 ['Refurbished Mac Pro 3.2GHz 16-core Intel Xeon W, Radeon Pro 580X', '$8,159.00'],
 ['Refurbished 27-inch iMac Pro 2.3GHz 18-core Intel Xeon W with Retina 5K display and Radeon Pro Vega 64X', '$8,239.00'],
 ['Refurbished Mac Pro 3.3GHz 12-core Intel Xeon W, Radeon Pro Vega II', '$8,579.00'],
 ['Refurbished Mac Pro 3.5GHz 8-core Intel Xeon W, Two Radeon Pro W5700X, Apple Afterburner', '$9,179.00'],
 ['Refurbished Mac Pro 3.2GHz 16-core Intel Xeon W, Radeon Pro 580X', '$10,789.00'],
 ['Refurbished Mac Pro 2.5GHz 28-core Intel Xeon W, Two Radeon Pro Vega II Duo', '$26,769.00'],
 ['Refurbished Mac Pro 2.5GHz 28-core Intel Xeon W, Two Radeon Pro Vega II Duo, Apple Afterburner', '$41,649.00'],
 ['Refurbished Mac Pro 2.5GHz 28-core Intel Xeon W, Two Radeon Pro Vega II Duo, Apple Afterburner', '$42,159.00'],
 ['Refurbished Mac Pro 2.5GHz 28-core Intel Xeon W, Two Radeon Pro Vega II Duo, Apple Afterburner', '$43,599.00']]
ipad
[['Refurbished iPad Air Wi-Fi 64GB - Gold (3rd Generation)', '$419.00'],
 ['Refurbished iPad Air Wi-Fi 64GB - Silver (3rd Generation)', '$419.00'],
 ['Refurbished iPad Air Wi-Fi 64GB - Silver (4th Generation)', '$469.00'],
 ['Refurbished iPad Air Wi-Fi 64GB - Sky Blue (4th Generation)', '$469.00'],
 ['Refurbished iPad Air Wi-Fi 64GB - Space Gray (4th Generation)', '$469.00'],
 ['Refurbished iPad Air Wi-Fi 64GB - Rose Gold (4th Generation)', '$469.00'],
 ['Refurbished iPad Air Wi-Fi 64GB - Green (4th Generation)', '$469.00'],
 ['Refurbished 11-inch iPad Pro Wi‑Fi 64GB - Space Gray', '$519.00'],
 ['Refurbished 11-inch iPad Pro Wi-Fi 64GB - Silver', '$519.00'],
 ['Refurbished iPad Air Wi-Fi 256GB - Gold (3rd Generation)', '$549.00'],
 ['Refurbished iPad Air Wi-Fi 256GB - Sky Blue (4th Generation)', '$599.00'],
 ['Refurbished iPad Air Wi-Fi 256GB - Rose Gold (4th Generation)', '$599.00'],
 ['Refurbished iPad Air Wi-Fi 256GB - Green (4th Generation)', '$599.00'],
 ['Refurbished iPad Air Wi-Fi 256GB - Space Gray (4th Generation)', '$599.00'],
 ['Refurbished iPad Air Wi-Fi 256GB - Silver (4th Generation)', '$599.00'],
 ['Refurbished 11-inch iPad Pro Wi-Fi 128GB - Space Gray (2nd Generation)', '$609.00'],
 ['Refurbished 11-inch iPad Pro Wi-Fi 128GB - Silver  (2nd Generation)', '$609.00'],
 ['Refurbished 11-inch iPad Pro Wi-Fi 512GB - Silver', '$769.00'],
 ['Refurbished 11-inch iPad Pro Wi-Fi 512GB - Space Gray', '$769.00'],
 ['Refurbished 11-inch iPad Pro Wi-Fi 512GB - Silver (2nd Generation)', '$859.00'],
 ['Refurbished 11-inch iPad Pro Wi-Fi 512GB - Space Gray (2nd Generation)', '$859.00'],
 ['Refurbished 11-inch iPad Pro Wi-Fi 1TB - Space Gray', '$939.00'],
 ['Refurbished 11-inch iPad Pro Wi-Fi 1TB - Silver', '$939.00'],
 ['Refurbished 11-inch iPad Pro Wi-Fi + Cellular 512GB - Space Gray (2nd Generation)', '$989.00'],
 ['Refurbished 11-inch iPad Pro Wi-Fi + Cellular 512GB - Silver  (2nd Generation)', '$989.00'],
 ['Refurbished 11-inch iPad Pro Wi-Fi 1TB - Space Gray (2nd Generation)', '$1,029.00'],
 ['Refurbished 11-inch iPad Pro Wi-Fi 1TB - Silver  (2nd Generation)', '$1,029.00'],
 ['Refurbished 11-inch iPad Pro Wi-Fi + Cellular 1TB - Silver', '$1,069.00'],
 ['Refurbished 11-inch iPad Pro Wi-Fi + Cellular 1TB - Space Gray', '$1,069.00'],
 ['Refurbished 12.9-inch iPad Pro Wi-Fi + Cellular 512GB - Space Gray (4th Generation)', '$1,129.00'],
 ['Refurbished 12.9-inch iPad Pro Wi-Fi + Cellular 512GB - Silver (4th Generation)', '$1,129.00'],
 ['Refurbished 11-inch iPad Pro Wi-Fi + Cellular 1TB - Silver  (2nd Generation)', '$1,159.00'],
 ['Refurbished 11-inch iPad Pro Wi-Fi + Cellular 1TB - Space Gray (2nd Generation)', '$1,159.00'],
 ['Refurbished 12.9-inch iPad Pro Wi-Fi + Cellular 1TB - Space Gray (3rd Generation)', '$1,179.00'],
 ['Refurbished 12.9-inch iPad Pro Wi-Fi + Cellular 1TB - Silver (3rd Generation)', '$1,179.00'],
 ['Refurbished 12.9-inch iPad Pro Wi-Fi + Cellular 1TB - Space Gray (4th Generation)', '$1,299.00']]
iphone
[['Refurbished iPhone 11 Pro 512GB - Silver (Unlocked)', '$919.00'], ['Refurbished iPhone 11 Pro 512GB - Space Gray (Unlocked)', '$919.00']]
watch
[['Refurbished Apple Watch Series 7 GPS, 41mm Starlight Aluminum Case with Starlight Sport Band', '$339.00'],
 ['Refurbished Apple Watch Series 7 GPS, 41mm Blue Aluminum Case with Abyss Blue Sport Band', '$339.00'],
 ['Refurbished Apple Watch Nike Series 7 GPS, 41mm Midnight Aluminum Case with Anthracite/Black Nike Sport Band', '$339.00'],
 ['Refurbished Apple Watch Series 7 GPS, 41mm Midnight Aluminum Case with Midnight Sport Band', '$339.00'],
 ['Refurbished Apple Watch Series 7 GPS, 45mm Green Aluminum Case with Clover Sport Band', '$359.00'],
 ['Refurbished Apple Watch Nike Series 7 GPS, 45mm Midnight Aluminum Case with Anthracite/Black Nike Sport Band', '$359.00'],
 ['Refurbished Apple Watch Series 7 GPS, 45mm Starlight Aluminum Case with Starlight Sport Band', '$359.00'],
 ['Refurbished Apple Watch Series 7 GPS, 45mm Blue Aluminum Case with Abyss Blue Sport Band', '$359.00'],
 ['Refurbished Apple Watch Series 3 GPS + Cellular, 42mm Stainless Steel Case with Soft White Sport Band', '$409.00'],
 ['Refurbished Apple Watch Series 3 GPS + Cellular, 42mm Space Black Stainless Steel Case with Black Sport Band', '$409.00'],
 ['Refurbished Apple Watch Series 7 GPS + Cellular, 45mm Starlight Aluminum Case with Starlight Sport Band', '$449.00'],
 ['Refurbished Apple Watch Series 7 GPS + Cellular, 45mm Midnight Aluminum Case with Midnight Sport Band', '$449.00'],
 ['Refurbished Apple\xa0Watch Series\xa05 GPS\xa0+\xa0Cellular, 44mm, Gold Stainless Steel Case with Stone Sport Band', '$499.00'],
 ['Refurbished Apple Watch Series 6 GPS + Cellular, 40mm, Graphite Stainless Steel Case with Black Sport Band', '$559.00'],
 ['Refurbished Apple Watch Series 7 GPS + Cellular, 45mm Gold Stainless Steel Case with Dark Cherry Sport Band', '$639.00'],
 ['Refurbished Apple Watch Series 7 GPS + Cellular, 45mm Graphite Stainless Steel Case with Abyss Blue Sport Band', '$639.00']]
appletv
[['Refurbished Apple TV HD 32GB', '$129.00'], ['Refurbished Apple TV 4K 32GB (2nd Generation)', '$149.00'], ['Refurbished Apple TV 4K 64GB (2nd Generation)', '$169.00']]
clearance
[]
accessories
[]
end scraper!
```
