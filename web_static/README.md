Tasks
0. Inline styling
Write an HTML page that displays a header and a footer.
Layout:
•	Body:
o	no margin
o	no padding
•	Header:
o	color #FF0000 (red)
o	height: 70px
o	width: 100%
•	Footer:
o	color #00FF00 (green)
o	height: 60px
o	width: 100%
o	text Best School center vertically and horizontally
o	always at the bottom at the page
Requirements:
•	You must use the header and footer tags
•	You are not allowed to import any files
•	You are not allowed to use the style tag in the head tag
•	Use inline styling for all your tags

 1. Head styling
Write an HTML page that displays a header and a footer by using the style tag in the head tag (same as 0-index.html)
Requirements:
•	You must use the header and footer tags
•	You are not allowed to import any files
•	No inline styling
•	You must use the style tag in the head tag
The layout must be exactly the same as 0-index.html
Repo:
•	GitHub repository: AirBnB_clone
•	Directory: web_static
•	File: 1-index.html

2. CSS files
Write an HTML page that displays a header and a footer by using CSS files (same as 1-index.html)
Requirements:
•	You must use the header and footer tags
•	No inline styling
•	You must have 3 CSS files:
o	styles/2-common.css: for global style (i.e. the body style)
o	styles/2-header.css: for header style
o	styles/2-footer.css: for footer style
The layout must be exactly the same as 1-index.html


3. Zoning done!
Write an HTML page that displays a header and footer by using CSS files (same as 2-index.html)
Layout:
•	Common:
o	no margin
o	no padding
o	font color: #484848
o	font size: 14px
o	font family: Circular,"Helvetica Neue",Helvetica,Arial,sans-serif;
o	icon in the browser tab
•	Header:
o	color: white
o	height: 70px
o	width: 100%
o	border bottom 1px #CCCCCC
o	logo align on left and center vertically (20px space at the left)
•	Footer:
o	color white
o	height: 60px
o	width: 100%
o	border top 1px #CCCCCC
o	text Best School center vertically and horizontally
o	always at the bottom at the page
Requirements:
•	No inline style
•	You are not allowed to use the img tag
•	You are not allowed to use the style tag in the head tag
•	All images must be stored in the images folder
•	You must have 3 CSS files:
o	styles/3-common.css: for the global style (i.e body style)
o	styles/3-header.css: for the header style
o	styles/3-footer.css: for the footer style

4. Search!
Write an HTML page that displays a header, footer and a filters box with a search button.
Layout: (based on 3-index.html)
•	Container:
o	between header and footer tags, add a div:
	classname: container
	max width 1000px
	margin top and bottom 30px - it should be 30px under the bottom of the header (screenshot)
	center horizontally
•	Filter section:
o	tag section
o	classname filters
o	inside the .container
o	color white
o	height: 70px
o	width: 100% of the container
o	border 1px #DDDDDD with radius 4px
•	Button search:
o	tag button
o	text Search
o	font size: 18px
o	inside the section filters
o	background color #FF5A5F
o	text color #FFFFFF
o	height: 48px
o	width: 20% of the section filters
o	no borders
o	border radius: 4px
o	center vertically and at 30px of the right border
o	change opacity to 90% when the mouse is on the button
Requirements:
•	You must use: header, footer, section, button tags
•	No inline style
•	You are not allowed to use the img tag
•	You are not allowed to use the style tag in the head tag
•	All images must be stored in the images folder
•	You must have 4 CSS files:
o	styles/4-common.css: for the global style (body and .container styles)
o	styles/3-header.css: for the header style
o	styles/3-footer.css: for the footer style
o	styles/4-filters.css: for the filters style
•	4-index.html won’t be W3C valid, don’t worry, it’s temporary


5. More filters
Write an HTML page that displays a header, footer and a filters box.
Layout: (based on 4-index.html)
•	Locations and Amenities filters:
o	tag: div
o	classname: locations for location tag and amenities for the other
o	inside the section filters (same level as the button Search)
o	height: 100% of the section filters
o	width: 25% of the section filters
o	border right #DDDDDD 1px only for the first left filter
o	contains a title:
	tag: h3
	font weight: 600
	text States or Amenities
o	contains a subtitle:
	tag: h4
	font weight: 400
	font size: 14px
	text with fake contents
Requirements:
•	You must use: header, footer, section, button, h3, h4 tags
•	No inline style
•	You are not allowed to use the img tag
•	You are not allowed to use the style tag in the head tag
•	All images must be stored in the images folder
•	You must have 4 CSS files:
o	styles/4-common.css: for the global style (body and .container styles)
o	styles/3-header.css: for the header style
o	styles/3-footer.css: for the footer style
o	styles/5-filters.css: for the filters style

6. It's (h)over
Write an HTML page that displays a header, footer and a filters box with dropdown.
Layout: (based on 5-index.html)
•	Update Locations and Amenities filters to display a contextual dropdown when the mouse is on the filter div:
o	tag ul
o	classname popover
o	text should be fake now
o	inside each div
o	not displayed by default
o	color #FAFAFA
o	width same as the div filter
o	border #DDDDDD 1px with border radius 4px
o	no list display
o	Location filter has 2 levels of ul/li:
	state -> cities
	state name must be display in a h2 tag (font size 16px)
Requirements:
•	You must use: header, footer, section, button, h3, h4, ul, li tags
•	No inline style
•	You are not allowed to use the img tag
•	You are not allowed to use the style tag in the head tag
•	All images must be stored in the images folder
•	You must have 4 CSS files:
o	styles/4-common.css: for the global style (body and .container styles)
o	styles/3-header.css: for the header style
o	styles/3-footer.css: for the footer style
o	styles/6-filters.css: for the filters style
 
7. Display results
Write an HTML page that displays a header, footer, a filters box with dropdown and results.
Layout: (based on 6-index.html)
•	Add Places section:
o	tag: section
o	classname: places
o	same level as the filters section, inside .container
o	contains a title:
	tag: h1
	text: Places
	align in the top left
	font size: 30px
o	contains multiple “Places” as listing (horizontal or vertical) describe by:
	tag: article
	width: 390px
	padding and margin 20px
	border #FF5A5F 1px with radius 4px
	contains the place name:
	tag: h2
	font size: 30px
	center horizontally
Requirements:
•	You must use: header, footer, section, article, button, h1, h2, h3, h4, ul, li tags
•	No inline style
•	You are not allowed to use the img tag
•	You are not allowed to use the style tag in the head tag
•	All images must be stored in the images folder
•	You must have 5 CSS files:
o	styles/4-common.css: for the global style (i.e. body and .container styles)
o	styles/3-header.css: for the header style
o	styles/3-footer.css: for footer style
o	styles/6-filters.css: for the filters style
o	styles/7-places.css: for the places style

8. More details
Write an HTML page that displays a header, a footer, a filter box (dropdown list) and the result of the search.
Layout: (based on 7-index.html)
Add more information to a Place article:
•	Price by night:
o	tag: div
o	classname: price_by_night
o	same level as the place name
o	font color: #FF5A5F
o	border: #FF5A5F 4px rounded
o	min width: 60px
o	height: 60px
o	font size: 30px
o	align: the top right (with space)
•	Information section:
o	tag: div
o	classname: information
o	height: 80px
o	border: top and bottom #DDDDDD 1px
o	contains (align vertically):
	Number of guests:
	tag: div
	classname: max_guest
	width: 100px
	fake text
	icon
	Number of bedrooms:
	tag: div
	classname: number_rooms
	width: 100px
	fake text
	icon
	Number of bathrooms:
	tag: div
	classname: number_bathrooms
	width: 100px
	fake text
	icon
•	User section:
o	tag: div
o	classname: user
o	text Owner: <fake text>
o	Owner text should be in bold
•	Description section:
o	tag: div
o	classname: description
Requirements:
•	You must use: header, footer, section, article, button, h1, h2, h3, h4, ul, li tags
•	No inline style
•	You are not allowed to use the img tag
•	You are not allowed to use the style tag in the head tag
•	All images must be stored in the images folder
•	You must have 5 CSS files:
o	styles/4-common.css: for the global style (i.e. body and .container styles)
o	styles/3-header.css: for the header style
o	styles/3-footer.css: for the footer style
o	styles/6-filters.css: for the filters style
o	styles/8-places.css: for the places style

9. Full details
Write an HTML page that displays a header, footer, a filters box with dropdown and results.
Layout: (based on 8-index.html)
Add more information to a Place article:
•	List of Amenities:
o	tag div
o	classname amenities
o	margin top 40px
o	contains:
	title:
	tag h2
	text Amenities
	font size 16px
	border bottom #DDDDDD 1px
	list of amenities:
	tag ul / li
	no list style
	icons on the left: Pet friendly, TV, Wifi, etc… feel free to add more
•	List of Reviews:
o	tag div
o	classname reviews
o	margin top 40px
o	contains:
	title:
	tag h2
	text Reviews
	font size 16px
	border bottom #DDDDDD 1px
	list of review:
	tag ul / li
	no list style
	a review is described by:
	h3 tag for the user/date description (font size 14px). Ex: “From Bob Dylan the 27th January 2017”
	p tag for the text (font size 12px)
Requirements:
•	You must use: header, footer, section, article, button, h1, h2, h3, h4, ul, li tags
•	No inline style
•	You are not allowed to use the img tag
•	You are not allowed to use the style tag in the head tag
•	All images must be stored in the images folder
•	You must have 5 CSS files:
o	styles/4-common.css: for the global style (body and .container styles)
o	styles/3-header.css: for the header style
o	styles/3-footer.css: for the footer style
o	styles/6-filters.css: for the filters style
o	styles/100-places.css: for the places style

10. Flex
Improve the Places section by using Flexible boxes for all Place articles


11. Responsive design
Improve the page by adding responsive design to display correctly in mobile or small screens.
Examples:
•	no horizontal scrolling
•	redesign search bar depending of the width
•	etc.

12. Accessibility
Improve the page by adding Accessibility support
Examples:
•	Colors contrast
•	Header tags
•	etc.

