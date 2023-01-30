# GymGeeks

  
![home page](/media/GymGeeksHome.jpg)


GymGeeks is an online gym shop for all your gym essentials - from gym equipment to activewear to supplements to exercise kits. A user can select from a wide range of gym equipment, activewear, supplements and exercise kits - that they can buy for themselves or gift to loved ones who loves to exercise. GymGeek kits are handcrafted specifically for individuals with different hobbies. For example, there is a running kit, boxercise kit etc to cater to a users specific interest. GymGeeks appeals to a wide variety of people - people who want to invest in good quailty active wear, people who want to buy gym equipment and people who want to gift their loved ones or themselves a fun active kit. 

- Superuser Details: 
    - gillian
    - potato12345678
     
# Features

## Existing Features

- Navigation Bar

   - Featured on every page this is a simple navigation bar. It is fully responsive and includes links to Home, Register, Login. It also offers a link to 'product management' if you are an account admin and 'my profile' if  you have registered as a user.  It is identical on each page to allow for easy navigation.
   - If the user is viewing the site a phone or tablet - the navigation becomes a simple burger menu. This allows for easy flow navigation. 
   - The logo 'GymGeeks' is also a clickable link to the homepage. This allows for easy navigation when the user views the site on a mobile or tablet device. 

  
![nav bar](/media/navbar2.png)

- Home

   - The homepage is simple and minimalist. It contains a 'shop now' button and a catchy slogan 'Shop & Gym' with an transparent image titled 'Workout.' The 'shop now' button links directly to GymGeeks catalogue of vairous products. I thought by keeping the style of the homepage minimalist with just a shop now button the user would be more likely to click the link than if there was a lot to read on the homepage itself. The navigation is at the top and footer with links to social media at the bottom of the page.

   - I modifed the design during development. I thought it would improve user experience by adding a clickable list. I thought this woud be eye-catching and the user would be more likely to click on these links than opening the products in the nav bar. I still kept the nav bar so the user could navigate between products when they are on the product detail page. I ended up changing this design right before submission as it was not responding well on mobile screens and more than likely users would review this on mobile. Hence, I got rid of the list and logo for a more clean minialist design. 

- Footer

   - The footer section includes links to relevant social media sites for GymGeeks. The links will open to a new tab to allow easy navigation for the user. 
   - The footer is valuable to the user as it encourages them to keep connected via social media, encouraging community among users.

   
![footer](/media/footer.png) 

- Register 

   - A user can register by clicking on the register link in the nav bar. 
   - The user is taken to the sign up page where they are instructed to sign up via email and enter their email and password twice. They also must create a username.
   - Email validation is in place requring an '@' sign and '.com, .co, .ie, etc.' The user must confirm their email before they can access GymGeeks.
   - Password validation is in place requiring 8 characters, no solely numeric value and common password. 
   - The user recieves a success message I implemented via 'toasts' once they sign up/in/out. They recieve an error message if they do not successfully sign in.  
   - There is a button for the user to submit their form, they are then signed up. 
   - This page will allow the user to sign up to GymGeeks.

  ![register](/media/sign-up.png) 

- Sign In

   - A user can login by clicking on 'My Account' link in the nav bar. 
   - The user is taken to the sign in page where they are instructed to sign in via email or username. If the user does not have an account they can sign up following the provided link. 
   - On the sign-in page the user can sign in using an email address and password. They can select "remember me" if they so wish. 
   - The user has to enter a valid email containing "@" and a valid password. 
   - I created password validation to require - a miniumum length, a numeric value and avoid common password. 
   - There is a button for the user to submit their form, they are then signed in and alerted that they are signed in. 

     ![register](/media/sign-in.png) 

- Product Page

  - The user can select which category they would like to view. Here they can look at each product, view their price, rating and title.
  - If they want to investigate a product further they can select it and then they will be guided to the individual product so they can read the product description description.
  - They can select the size of their product (if the product has a size)

      ![register](/media/products.jpg) 

- Basket/Checkout 

   - The user can navigate to the checkout by clicking on their basket. 
   - The user can then view their basket and see the amount it has complied to. 
   - They can then decide to 'keep shopping' or proceed to 'secure checkout.' 
   - The checkout page contains a simple form. 
   - The user must fill out their delivery details and card details.
   - Vaild card details are required, for instance enough numbers and no letters. 
   - The page is simple and minialist, allowing ease of navigation and an enjoyable user experience. 

     ![shopping](/media/shopping-bag.jpg) 
     ![checkout](/media/checkout.jpg) 


- Product Management 

  1. Super User
   - If the user is a Super User, they can login and edit the site via 'Product Management' link under 'My Account' in the nav bar.  
   - This is a neat form where the admin can add, edit or delete their products.
   - The admin here has full CRUD functionalities.
   - The admin can also see user enquires here from customers.
   - They can read and delete the enquires listed in a table.
   - This allows ease of access and flow for admins instead of using the Django backend framework. 

    ![edit/delete](/media/edit_delete.jpg) 

    ![dropdown](/media/dropdown.jpg) 

    ![product_management](/media/product_management.jpg) 

   2. Account Owners
   - If a user signs up for an account they have access to their user profile. 
   - Here they can view their product history, delivery details and what items are in their wishlist. 
   - They can add products to their wishlist and delete items from their wishlist.
   - They can leave reviews on products, rate them out of 5 and delete their own review.
   - They can leave an enquiry through the contact form. 

   3. Non-Account Owners
   - Non-account owners can view the site and its products.
   - They cannot leave reviews, rate products or add items to a wishlist.
   - They are prompted to sign up in order to access these features. 
   - They can leave an enquiry through the contact form. 

- Wishlist

 - Users can add products to their Wishlist, if they do not wish to purchase items straight away. This is located at the top of the users profile page. 
 - The products will remain in the users Wishlist until they have purchased the item or removed it from the list.

 ![wishList](/media/wishList.jpg) 

 ![wishList](/media/add_wishlist.jpg) 
 
- 404 page

 - I implemented a 404 page with an appropriate redirect back to the product shop page in case the user attempted to access non-existent content. 
 - To see this page please use this url - https://gymgeeks.herokuapp.com/test

 ![404](/media/404.jpg) 

- Contact Form

 - A user can open up the contact form by clicking on the "Contact Us" tab in the nav bar.
 - If the user is logged in, the email field is prepopulated with the user's email address.
 - The form contains a drop down menu where the user can select the type of enquiry from a list so that the site owner knows what the enquiry is about.
 - The user must fill out all the fields. If the form is submitted with any of these fields left blank they will be allowed proceed.
 - When the form is submitted, the user receives an email confirmation of their enquiry so that they have a record of it.
 - The form is submitted to the site owner who can access it when they login to GymGeeks via 'enquries' panel in the dropdown under 'my account' or they can access it through Django Admin. 

  ![contact_us](/media/contact_us.jpg) 


  ![contact_us](/media/enquiry_type.jpg) 

- Product Review

 - A logged in user can leave a review on a product.
 - They do not have full CRUD functionality due to time constraints I could not implemenent this - but they can delete their review and a super user can also delete their review.
 - They can rate the product out of 5.
 - If a user does not have an account they are prompted to sign up to leave a review. 
 - Reviews are visible to everyone. 

 ![product_review](/media/product_review.jpg) 

 ![product_review](/media/sign-in-review.jpg) 

- Stripe

 - I implemented Stripe in test mode. Below are the credentials that can be used to make a 'fake' payment and test that all systems are working as they should.

  ![stripe](/media/stripe.jpg) 

# Other Technologies

- Gitpod as the IDE
- Git used for version control via the terminal in Gitpod
- GitHub used to store the code in the repository
- ElephantSQL was used as the cloud based platform for deployment
- Fontawesome for icons
- Google images & Pexel for images
- Canva for Facebook Business Mock-up
- Google Chrome Dev Tools for inspection during development to check reponsiveness and contrast.
- Favicon.io for the favicon
- W3C Markup Validation Service
- Lucid Charts for design mock-ups & dataschema

# Agile Development Methology:

 - I documented and implemented all User Stories using the Agile Project Management tools on GitHub. 
 - I created a basic kanban board in the projects section of my git-hub repository.
 - Here I created User Stories using the CI template - AS A - I WANT - SO THAT. 
 - I linked them with my project and moved them into the to do section of my kanban board.
 - I labelled my User Stories in accordance with MoSCow prioritization.  
 - I researched and asked friends and family who had an interest in fitness what they would want from a fitness shop/gym and whether a combination of both was a good idea and if it was something they would enjoy themselves. 
 - I asked them to write some User Stories to see if they came up with ones I hadn't thought of. 
 - I kept my site simple to ensure all the functionality ran smoothly and efficiently, keeping continious attention to technical proficiency. 
 - To start, I chose between one - three 'Must Have' user stories and moved them into the 'in progress' board and continued from there, starting with the 'must have' stories first with some others that over-lapped moving on to the 'should have' and then 'could have' depending on my time frame and scope. Towards the end of my project I changed some to 'won't have' as this time frame and scope did not let me implement certain things like a booking system and class timetable.

# Scope

The scope of this project was very large at the planning stage. The ultimate goal was to create an e-commerce site that combined a Gym club and an active wear/gym equipment shop. Thus, an all in one GymHub. The site must allow users to complete a purchase on my e-commerce store and for everything to run smoothly in this process. This meant - payment was processed, email reciept with details, order history evident in logged in user profile and abandoned baskets were remembered if a user was logged in. This also meant if a user was an admin they had full CRUD functionality on store products. Thus, they would be able to access 'product management' on login and edit, delete and create products for the store instead of using Django admin. This allowed for a smoother process for potential employees and a nicer user experience. This was all achieved within this project.

In addtion, I wanted to encourage an online community with my site for users to chat to each other and get to know the GymGeeks team but time constraints meant I was not able to implement this further functionality. However, via the Facebook business account community could be encouraged and if I was to see a vision for GymGeeks this is where the bulk of community would exist via posting and sharing and commenting - the GymGeek site itself would solely act as a e-commerce gym shop. I wanted to implement a subscription service/nutrition plans but again time constraints and personal health issues prevented me from doing so. I would have liked to implemented 'live available classes timetable' and a page to get to know the team. In the end I thought it was best for GymGeeks to act as a all in one gym shop with active-wear, gym equipment and supplements - the active user won't need to go anywhere else! GymGeeks has a clear focus on gym essentials - e.g equipment, active wear and supplements for people who do not have time or the money to join a gym or prefer to work out at home or outside. I also thought to add 'kits.' I thought this was a good marketable ploy for customers to gift their loved ones who have an interest in activties such as boxing or yoga. 

# Structure

The site consists of 11 pages: Home, register, sign-in, products (x4 categories currently), shopping basket, checkout, product management. All pages can be viewed by all users, apart from product management which can only be viewed by a site admin. 

# Epics and User Stories
 - I had 8 Epics:

 1. Epic: Set up admin page for admin to have full CRUD functionality on products and categories, and view customer orders/sign ups. 
 2. Epic: Enable users to set up an account on the site to have full access to features. 
 3. Epic: Create minialist eye-catching home page. 
 4. Epic: Enable registered users to be able to view their purchase history, remember card details and remember abandoned baskets. 
 5. Epic: Implement Stripe to enable users to be able to pay for their items on checkout. 
 6. Epic: Enable users to able to view, filter, search products/categories based rating, price, deals, clearance and name to enhance UX.
 7. Epic: Set up Facebook Business Page to enable users to make contact with each other and engage in a community where they can view fitness posts/offers from GymGeeks. 
 8. Epic: Enable admin to be able to use full CRUD functionality on the site itself after account registration.  

 - I had 27 User Stories in total and moved them in accordance with whether they were in progress or completed. Here are my User Stories:

           - As a Shopper I want the ability to book a class on the site so that I can make sure to get my slot and see what timetable classes are available on a weekly basis

           - As a Shopper I want the ability to read about GymGeek staff so that I can get a feel for who GymGeek are and what they offer

           - As a Shopper I want the ability to purchase a subscription to gym classes/membership so that I can easily sign up to GymGeek classes or membership

           - As a Admin I want the ability to easily delete/edit products* so that I can easily set up my site

           - As a Shopper I want the ability to easily select the quantity* so that I can ensure I don't accidentally select the wrong quantity

           - As a Shopper I want the ability to easily select the size* so that I can ensure I don't accidentally select the wrong product size

           - As a Shopper I want the ability to easily see what I have searched for and the number of results so that I can quickly decide whether the product I want is available

           - As a Shopper I want the ability to Search for a product by name or description so that I can find a specific product I'd like to purchase

           - As a Shopper I want the ability to sort through multiple categories of products simultaneously so that I can find the best priced or rated products across broad categories such as 'active wear' or 'gym equipment'

           - As a Shopper I want the ability to sort through multiple categories of product so that I can find the best priced or rated in a specific category or sort the products in that category by name

           - As a Shopper I want the ability to sort through a specific category by name so that I can select the category I want and view only items in this category

           - As a Shopper I want the ability to search through a specific category of products so that I can find the best-priced or best-rated product in a specific category

           - As a shopper I want the ability to sort and filter through the list of available products so that I can easily identify the best rated, best priced and separate categories

           - As a Site User I want the ability to have a personalised user profile so that I can view my personal order history and order confirmations and save my payment information

           - As a Site User I want the ability to receive email confirmation after registering my account* so that I can verify my account registration was successful

           - As a Site User I want the ability to recover & reset my password so that I can **recover access to my account **

           - As a Site User I want the ability to Easily login and out so that I can **have security and access my personal account information **

           - As a Site User I want the ability to view my profile so that I can **view my order history **
           
           - As a Site User I want the ability to view my profile so that I can **see my account details **

           - As a Site User I want the ability to Easily register for an account so that I can **have a personal account **

           - As a shopper I want the ability to learn more about GymGeeks so that I can get an incite to the company

           - As a shopper I want the ability to navigate clearly through the site so that I can have a good user experience

           - As a shopper I want the ability to easily view the total of my purchases at any time so that I can avoid spending past my budget

           - As a shopper I want the ability to quickly identify deals, clearance items and special offers so that I can take advantage of special savings on products I'd like to purchase

           - As a shopper I want the ability to view products individually so that I can Identify the price, description, product rating, image and potentially sizes available

           - As a shopper I want the ability to view a list of products so that I can select some to purchase

 - I labelled them with MoSCow prioritization so that this allowed me to prioritise certain tasks to implement over less important tasks depending on time and scope. 


# Data Models

The following models have been used to populate the database and for the site to function as it should:

* **User** - the built in Django User model, facilitates the users basic information

* **Category** - the category in which the product is placed

* **Contact** - a model for users to contact admin with a query

* **Product** - the model for the product itself and its details

* **Review** - a model for users to give the product a rating and a review

* **Order** - a users successful purchase leads to an instance of the Order model being created, storing delivery and user data

* **OrderLineItem** - a model holding the product information for a single product, binding the product model together with the order

* **UserProfile** - the model storing the users product and order information

* **WishListItem** - the customer has the option to save an item, which will then appear in their wish list on their GymGeek user profile

* **NewsLetterSignUp** - the customer can sign up to GymGeeks using a mail chimp pop-up

# Testing

## Manual Testing:

 - I chose to manually test my project as my app is small and not so complicated. If my project was bigger and if I decide to continue with developing this app further I would consider automated testing as manual testing for a larger project has a high error rate and probably would not suffice by itself. For this project I believe manual testing was all that was needed. 

 - I began my manual testing by checking that my project works according to user stories, this is known as BDD - Behaviour Driven Development where the result is based on an expected outcome. This type of testing bulids from user stories where I would sit in front of my app and test it to see if it behaves as expected. Similar to user story template - AS - I WANT - SO THAT - I created a number of atomic tests by using the template - GIVEN - WHEN - THEN. This template describes the outcome in a testable way. 
 
 ## Atomic Tests
 
 - My tests were written for both the user and admin. They read as follows:

          -  AS a *Site User* I WANT the ability to receive email confirmation after registering my account* SO THAT I can verify my account registration was successful

           - AS a *Site User* I WANT the ability to recover & reset my password SO THATI can **recover access to my account **

           - AS a *Site User* I WANT the ability to easily login and out SO THAT I can **have security and access my personal account information **

           - AS a *Site User* I WANT the ability to view my profile SO THAT I can **view my order history **
           
           - AS a *Site User* I WANT the ability to view my profile SO THAT I can **see my account details **

           - AS a *Site User* I WANT the ability to easily register for an account SO THAT I can **have a personal account**

           - AS a *shopper* I WANT the ability to learn more about GymGeeks SO THAT I can gain insight to the company

           - AS a *shopper*  I WANT the ability to navigate clearly through the site SO THAT I can have a good user experience

           - AS a*shopper*  I WANT the ability to easily view the total of my purchases at any time SO THAT I can avoid spending past my budget

           - AS a *shopper*  I WANT the ability to quickly identify deals, clearance items and special offers SO THAT I can take advantage of special savings on products I'd like to purchase

           - AS a *shopper*  I WANT the ability to view products individually SO THATI can Identify the price, description, product rating, image and potentially sizes available

           - AS *shopper* I WANT the ability to view a list of products SO THAT I can select some to purchase


 ## Example of running Atomic Test:

 - User Story:


   - AS A *User* I WANT *the ability to easily view the total of my purchases at any time* SO THAT *I can avoid spending past my budget*
   - AS A *User*  I WANT *the ability to sort through a specific category by name* SO THAT *I can select the category I want and view only items in this category*

   - GIVEN *That a user is on any site page* WHEN *the user has added an item to the bag* THEN *The user is able to see the total cost of their basket*
   - GIVEN *That a user is on any site page* WHEN *the user has typed in their specific category into the search bar* THEN *The user is able to naviagate directly to their desired product if available*

 - Testing Steps:

  1. I navigate to GYMGEEKS site
  2. I am on the product page
  3. I click on a product and add it to the basket

 - Expected Result: 

   - The basket icon in the corner of the top right screen turns blue and the amount of the added item is visible - informing the user of how much their basket is costing. 

 - Actual Result:

   - The basket turns blue, the item is added to cart and the number increasing according to the price of the porduct/products. 

- Pass or Fail:
   
   - Atomic test *passes* because expected result matches actual result. 

- I went through each User Story following the template above and accounted for whether the test failed or passed in conjunction with my GIVEN-WHEN-THEN template. If it passed my test was valid and I could move on to the next one. If it failed I had to go back to development and resolve the issue.  

## Other Forms of Testing
 
- I tested if my project worked on different browsers such as - Google Chrome, Safari, Microsoft Edge and Firefox - with different resolutions. 

- I tested if my project was responsive on a number of different devices- mobile, tablets, desktops from 320px to 1201px. I used developer tools to make sure my site works on all device sizes. 

- I sent my deployed link to friends and family to double check that it worked adequately on all different types of screens.

- I tested my site on the website - responsive design checker- which ran my site through a variety of different screen sizes and devices. I inspected each one and was happy with the level of responsivity.

- I tested my site in dev tools lighthouse and was happy with the result.


## Validator Testing 

- HTML
   - No errors were returned when passing through the official W3C validator

- Terminal
   - I went through my terminal errors line by line and tided up any issues or problems. 
   - To see all errors at once I used flake8 in my terminal. This made it easier to work through each issue as it took me directly to the line in which the issue was present.

- Validator
  - Due to time constraints I was not able to fully test ny code in all vaildators. Tutor support said it is best to just fixed the issues in the terminal given the time pressue I was under. 

## Unfixed Bugs

- I had a lot of errors when I attempted to set up my facebook business account. I made 3 separate social media accounts to create this page but facebook kept blocking it after a few minutes.  
- Instead I modified an already existing Facebook Business Page and edited to fit my site using Canva.
- The product images became hidden under the footer in some views - thus I added a overflow scroll and max-height which prevents this now from occuring.
- In mobile view the top to move the user to the top of the screen overlaps with go to cart. I found this bug last minute and I was unable to remove it in time.
- I was unable to implement full CRUD functionality for the user who leaves a review - they should be able to edit their post but all I managed to implement was the ability to create and delete posts. I would have also liked to have implemented that the post would go to the admin first for approval but I did not notice this until a friend pointed it out and by then it was too late. 

## Marketing 

- SEO 

I used SemRush to generate keywords which I then implemented in my meta-tags in head of base.html file. I inserted a meta-tag description and gave it a basic sum-up og GymGeeks site. I named my images in my media folder with accurate names so SERPS can read them better. I added keywords to the meta-tag that will increase my sites appearance on google. SemRush is a handy free tool that can be used to best optimise your choice of keywords. It is free but with limited number of times a day you can use it. I found this very useful in generating keywords rather than spending hours researching what words would be best. 

I input a sitemap within my site. This helps search engines discover URLS on the site which is particurly useful if you have a large site. I generated this sitemap using the site 'XML-Sitemaps.com'. I created a robot.txt file - this tells the search engine crawlers which URLs the crawler can access on your site. This is used mainly to avoid overloading sites with requests. I generated this file here 'https://en.ryte.com/free-tools/robots-txt-generator/'

- Content Marketing

Within my project I implemented content marketing techniques such as offers, deals and free delivery over a certain threshold. I also created a FaceBook Business page. This is where the bulk of content marketing would occur - through posting offers, discounts and engaging users whether in raffle competitons or data-driven polls. This Facebook page could also host blog posts, videos snd newsletters - letting the customer know the latest offers. This marketing stratgey gains attention, sales and increases brand awareness and growth. I believe the Facebook page could also be used for organic growth by building a community and increasing customer loyalty and trust.

- Business Model

GymGeeks is a B2C business. It is an e-commerce store that sells directly to the customer. There is an open market for getting active and encouraging well being, this sector is becoming more and more popular as people start taking action with their health. Thus, I thought what could be more convient than a shop that sells, gym-equipment/clothes (to get active) and supplements (to get healthy). Plus the added benefit of kits - Is your friend a fan of running? Why not buy a 'Running-Kit'! My prognosis is if there was a one stop shop where one could take care of their health and overall well beinh - GymGeeks could be that.  It attracts people who are interested in getting active. I added on a category of 'kits' as a marketing stragety to encourages users to gift a loved one an 'active' present. This encourages well-being and health which is a market that is becomimg increasingly more popular.

If I was to work further on this project I would implement Google Analytics on GymGeeks to gain a better understanding of SEO so that we could tailor our keywords more efficeintly and thus market my site more adequetly. I would also look into paid ads or promotions - gaining an Influencer especially for a gym/clothes brand would gain serious traction and definetly an angle I would look in to. 

Presently and also due to time constraints - GymGeeks marketing stragety would mainly be through content marketing. This would be done through the Facebook Business Page. I implemented a footer at the end of my site to encourage users to follow the link to the site. Here the bulk of marketing would be done through content creation. Also encouraging the user to create an account in GymGeeks increases loyalty of the customer as they can come back, view their purchase history and potentially purchase again with ease as the site has remembered their address and card details (if choosen so). Having the added function of abandoned basket encourages the user to come back and shop. When the user goes on the site again and the items are still in their basket - thus this has the capability to increase sales. 

If I had more time and was not in bad health, I would have liked to implement mailchimp pop-up so that the user can sign up and recieve GymGeeks newsletter of offers and deals. I would have also marketed the kits better. I think as of now they are lost in the site and there should have been a better technique put in for those kits to be more eye-catching and marketed as a gift. However, I am happy with the marketing stragety that is currently in place. I think with the combination of a facebook business page, a minimal user interface and SEO implementation - this site has enough marketing capabilites to reach the target audience. 



## UX Design 

- I implemented UX design when developing my project. I did so by putting myself in the users shoes and designed the site based on their needs. This site is for users interesed in exercise and health. It is targeted towards a user who wants to join a community for improving their fitness but also the ability to purchase active wear and gym equipment/classes - so it is an all in one gym.
- I viewed other gym and health websites to gain inspriation on what design fits best for this type of website. 
- I made sure my site was accessible by making sure all text is readable and that there is a right amount of contrast between colours. 
- I selected the colour pallet yellow, black and white as I thought it reflected strength and agility colours which would be assoicated with fitness and energy. These hard colours are strong and inviting but also smart and serious. 
- I made sure my site was simple as a design principle for an ease in terms of user experience. 
- I selected a simple readable, pleasing font to make sure my text was easily and quickly readable. 
- I provided ease of navigation so that the user can go back and forth between the homepage, browse merchandise, basket/checkout and profile. I also provided the ability for the user to have their own profile so that they can access their purchase history and update their address/contact details. 
- I created a favicon icon with the intials of my site 'GG'. I used an eyecatching font and stuck with the pallet of my site.
- I had implemented a 'workout' image/logo on the homepage but changed this before submission as it did not look good or go with the flow on a mobile device. Users are more likely to be looking at this site via mobiles so I removed this. I did keep it in my Facebook Business Page as I thought it looked good and more professional and did not disturb the flow. 

## Color Scheme

- I selected the colour pallet yellow, black, grey and white as I thought it reflected strength and agility colours which would be assoicated with fitness and energy. These hard colours are strong and inviting but also smart and serious. 
- These colors were also accessible with the rght amount of contrast between colours allowing for good readability. 
- I took inspiration from this grip sock site https://eos-elite.com/

![Design-Mockup2](/media/color-scheme.png) 

## Typography 

- I choose Lato font due to its round edges and the approachable warmth it gives to the user. It's now one of the most popular fonts on Google font and widely used pretty much everywhere. This typeface is highly used on websites to deliver information directly.
- I personally liked the light style which gave my site a clean modern look to its headings and body. It has a softer appearabce than Sans and for that reason I considered it more appealing. 

## Design Phase One
- I created multiple mock-ups of my site homepage - the landing page - as this is the most important page for the user as it is where they will make the decision to shop or not. I made sure it was minimalistic and had an easy flow. My site changed multiple times due to responsiveness issues, thus before submission I changed the design again so that it would display well on all screens. In hindsight, I would have created my first design on a mobile so that I would not have to worry about responsive issues. This caused a lot of problems at the end of my project.

![Design-Mockup](/media/design_mockup.jpg) 

- This is my first design. I followed the boiler plate CI Boutique Ado, modifying it to suit my store. I added my logo and shop name to the left, with a search bar to filter through products in the center and my basket icon set to the right hand corner. I added a 'workout' image to reflect the idea behind the site which is - to get active and exercise! I also thought having a staple image would make my site recognizable, from a marketing view point to have this flow would be userful and marketable.  I liked the idea of implementing a clickable list of items on the homepage. I thought this would be eye-catching and tempt the user to navigate to the products page. I also added a large selection of navigation items in the header of my website as at this point my scope was much larger. I added social media links within the footer so the user can naviagte more freely to GymGeeks different social media pages. 

## Design Phase Two

- My second design involved the removal of the list as this did not respond well on mobile devices and could not be fixed due to time constraints and scope. I also got rid of some of my nav items as I felt there was too much and it could be reduced down to just 4 tabs to accomdate all my items. I believed having 4 well working tabs was better than having 8 half-working tabs.

![Design-Mockup2](/media/design_mockup2.jpg) 

## Design Phase Three

- My third design involved the removal of the workout image as I did not like how it looked on mobile devices and I did not have time to play around with a new design for mobile. I took a 'one-size' fits all approach to the remainder of my design, taking a minimalist approach so the user would not be overwhelmed and easily navigate through this e-commerce site. 


![Design-Mockup3](/media/design_mockup3.jpg) 

# Mobile Design 

- As I said above, in hindsight I should have designed my site with mobile design first as my desktop design caused a lot of issues in the end. I decided to stay minimalist and keep both desktop and mobile simple so that it would not interfer with responsiveness. Having a functioning, responsive site was my main goal for this site. 

## Phase One

- After I created my first desktop design I viewed this on mobile in dev tools. I found the layout on mobile was too crowded. Although I liked the idea of a clickable list and workout logo image, overall it was not user friendly and so these did not make it to the second phase. 

![Design-Mockup1](/media/design_1.jpg) 

## Phase One

- In this phase of design I got rid of the list put kept the image. I found the image looked out of place and made the site look a little cheap and unsophisticated and so this did not make it to the final mobile design.

![Design-Mockup2](/media/design_2.jpg) 

## Phase Three

- As I said above - I took a 'one-size' fits all approach to the remainder of my design, taking a minimalist approach so the user would not be overwhelmed and easily navigate through this e-commerce site. 

![Design-Mockup3](/media/design_3.jpg) 

![Design-Mockup3](/media/mobile.jpg) 




## Database Schema for models - GymGeeks

- Below is a schema of models used in this application, created with Lucidchart.

![Database_schema](/media/Database_Schema_GymGeeks.png) 

## Facebook Business Page

![Facebook-Mockup](/media/facebook.png) 

- I implemented a mock up of a Facebook business page. I attempted to create an account numerous times but it kept getting shut down due to Facebook security so in the end I created a mock up in Canva to envision what GymGeeks business page would look like. I placed the logo 'workout' stamp as the icon/slogan and implemented it on the image of Facebook posts. I implemented it as such to keep the flow of the page and my site, linking it with the 'workout' stamp. I thought if it was used and placed regularly it would make my site more marketable and recognizsable. I envision this page to be a hub for community amongst GymGeek users. For users to find gym offers, subscriptions, classes or active-wear deals.  

## Mail Chimp Newsletter 

- I implemented a pop-up mailchimp newsletter sign-up to action itself when the user opens the homepage of the site. I implemented GymGeeks logo in this pop-up and asked for 'email.' The less forms to fill out the more likely a user will fill out this form. I created this pop-up to increase my users/following. This is a useful approach in the marketing world. 

- Each subscriber is registered in gymgeeks mail chimp account, thus these emails can be used for marketing purposes. 

![Newsletter-signup](/media/newsletter_signup.png) 

## Final Project

- My design changed a lot throughout this project, I had placed the image 'workout' logo on the homepage but decided to remove it as it did not suit the mobile view.  
- If I had more time I would have liked to add an image that could have worked on this homepage - one that suited all views and went with the flow.  

# Deployment 

I took the following steps to begin my deployment:

1. I installed Django and the supporting libraries.
2. I created a new blank Django project and app.
3. I set my project to using AWS (where my images would be stored) and ElephantSQL (relational database management system). 
4. Deployment came into difficulty when Heroku stopped offering free accounts and so I had apply for a student gitpod starter pack and export my older projects data to ElephantSQL. Luckily I had not yet deployed my PP5 by this point so I did not have to migrate my files to a new database. ElephantSQL was all hooked up before I began deployment.
5. I created an app named 'GymGeeks' and gave it the location - 'Europe.'
5. By following the steps outlines by Code Institute I added ElephantSQL as my database in the Resources tab of my app - I migrated my older data from Postgres to ElephantSQL. 
6. I copied the DATABASE_URL from my Config Vars and added it to my env.py file to link my new database_url with my Heroku app.
7. I created my SECRET_KEY in my environ.py file to encrypt session cookies and added this to my Heroku app config vars.
8. I then imported dj_database_url, os and added my SECRET_KEY and DATABASES to my settings.py file.
9. I migrated my files. 
10. I created a AWS bucket to store my images/media/static- I linked this URL to my env.py file and my Heroku app config vars.
11. In my settings.py file I added the required details for AWS to work.
12. After linking Django to AWS, adding my Templates Directory, creating my three directories - media, static and templates, adding a Procfile (web: gunicorn gymgeeks.wsgi) and adding my heroku app to ALLOWED_HOSTS in my settings.py file- I was then ready to make my first deployment to Heroku. 
13. In the deployment tab of my app I connected GitHub to my deployment method. 
14. I then connected my app to my GitHub repository and deployed it to my main branch. 
15. I watched the buliding log and when it was complete I selected 'open app' and my app successfully deployed. 
16. On final deployment I set "DEBUG = False". 

# Credits

- Thank you to friends and family for putting up with me through the last rounds of this diploma and helping me through tough times. 
- Thank you to my mentor for his guidance. 
- Thank you to tutor support for lending me a hand.
- Thank you to student care for your kindness.
- Thank you Code insitute for your support and their well detailed and informative Boutique Ado which was the basis for my project.
- Credit to past Code Insitute students John Venkiah and Ali O'Keefe for inspiration and guidance on models and design -https://aliokeeffe-pp5freshnest | https://github.com/johnvenkiah/CI_PP5_John_Venkiah
- Credit to https://eos-elite.com/ for design inspiration
- Thanks to Ger from student support specifically for guiding me through this last assignment