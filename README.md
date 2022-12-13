# GymGeeks

GymGeeks is an all in one gym shop and training centre. GymGeeks offers a wide variety of activewear, shoes, gym equipment and hand crafted protein shakes. They also offer a wide variety of classes that can be bought by individual users or in a package subscription deal. GymGeeks appeal to a wide variety of people - people who want to invest in good quailty active wear, people who want to join a gym or start some classes, people who have an interest in being active and joining a community.

# Features

## Existing Features

- Navigation Bar

   - Featured on every page this is a simple navigation bar. It is fully responsive and includes links to Home, Register, Login. It also offers a link to 'product management' if you are an account admin and 'my profile' if  you have registered as a user.  It is identical on each page to allow for easy navigation unless the user logs in then obviously the 'register' link disappears. 
   - If the user is viewing the site a phone or tablet - the navigation becomes a simple burger menu. This allows for easy flow navigation. 
   - The logo 'GymGeeks' is also a clickable link to the homepage. This allows for easy navigation when the user views the site on a mobile or tablet device. 

  
![nav bar](/media/PP4/nav.png) 

- Home

   - The homepage is simple and minimalist. It contains a 'shop now' button and a catchy slogan 'GymGeeks, more than just a gym....Grain & Train' with an transparent image titled 'Workout. The 'shop now' button links directly to GymGeeks catalogue of vairous products. I thought by keeping the style of the homepage minimalist with just a shop now button the user would be more likely to click the link than if there was a lot to read on the homepage itself. The navigation is at the top and footer with links to social media at the bottom of the page.

   
![homepage](/media/PP4/Home.png) 

- Footer

   - The footer section includes links to relevant social media sites for GymGeeks. The links will open to a new tab to allow easy navigation for the user. 
   - The footer is valuable to the user as it encourages them to keep connected via social media, encouraging community among users. 
   - The footer sticks to the bottom of the page and is located on every page of this site. 

   
![footer](/media/PP4/footer.png) 

- Register 

   - A user can register by clicking on the register link in the nav bar. 
   - The user is taken to the sign up page where they are instructed to sign up via email and enter their password twice. 
   - Email validation is in place requring an '@' sign and '.com, .co, .ie, etc.'
   - The user recieves a success message I implemented via 'toasts' GymGeeks once they sign up/in/out. They recieve an error message if they do not successfully sign in.  
   - There is a button for the user to submit their form, they are then signed up. 
   - This page will allow the user to get signed up to GymGeeks to start their fitness journey.

  ![register](/media/PP4/register.png) 

- Login

   - A user can login by clicking on the login link in the nav bar. 
   - The user is taken to the sign in page where they are instructed to sign in via email or social media. If the user does not have an account they can sign up following the provided link. 
   - On the sign-in page the user can sign in using an email address and password. They can select "remember me" if they so wish. 
   - The user has to enter a valid email containing "@" and a valid password. 
   - I created password validation to require - a miniumum length, a numeric value and avoid common password. 
   - There is a button for the user to submit their form, they are then signed in and alerted that they are signed in. 

# Other Technologies

- Gitpod as the IDE
- Git used for version control via the terminal in Gitpod
- GitHub used to store the code in the repository
- ElephantSQL was used as the cloud based platform for deployment
- Fontawesome for icons
- Google images & Pexel for images
- Lucid for wireframes
- Canva for Facebook Business Mock-up
- Google Chrome Dev Tools for inspection during development to check reponsiveness and contrast.
- Favicon.io for the favicon
- W3C Markup Validation Service
- W3C CSS Validation Service(Jigsaw) 
- PEP8 Online Checker

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

![kanban board](/media/PP4/kanban_board.png) 

# Scope

The scope of this project was large at the planning stage. The ultimate goal was to create an e-commerce site that combined a Gym club and an active wear/gym equipment shop. Thus, an all in one GymHub. The site must allow users to complete a purchase on my e-commerce store and for everything to run smoothly in this process. This meant - payment was processed, email reciept with details, order history evident in logged in user profile and abandoned baskets were remembered if a user was logged in. This also meant if a user was an admin they had full CRUD functionality on store products. Thus, they would be able to access 'product management' on login and edit, delete and create products for the store instead of using Django admin. This allowed for a smoother process for potential employees and a nicer user experience. I wanted to encourage an online community with my site for users to chat to each other and get to know the GymGeeks team but time constraints meant I was not able to implement this further functionality. However, via the Facebook business account community could be encouraged and if I was to see a vision for GymGeeks this is where the bulk of community would exist via posting and sharing and commenting - the GymGeek site itself would solely act as a e-commerce gym shop and gym-fitness subscription service. I would have liked to implemented 'live available classes timetable' and a page to get to know the team but time constraints affected on implementing this. 

# Structure ?

The site consists of 6 pages: Home, Sign-up/Sign-in, shop (x3 currently). All pages can be viewed by all users. The ability to comment/like posts is limited to logged in users. 

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

- I tested my site in dev tools lighthouse and was happy with the result:

 ![lighthouse](/media/PP4/lighthouse.png) 


## Validator Testing 

- HTML
   - No errors were returned when passing through the official W3C validator

- CSS
   -  No errors were returned when passing through the official Jigsaw validator

- Python
   - No errors were returned when passing through the PEP8 online check. 

- Javascript 
   - No errors were returned 

   ![html-validator](/media/PP4/validator.png) 

## Unfixed Bugs

- I had a lot of errors when I attempted to set up my facebook business account. I made 3 separate social media accounts to create this page but facebook kept blocking it after a few minutes.  

## UX Design 

- I implemented UX design when developing my project. I did so by putting myself in the users shoes and designed the site based on their needs. This site is for users interesed in exercise and health. It is targeted towards a user who wants to join a community for improving their fitness but also the ability to purchase active wear and gym equipment/classes - so it is an all in one gym.
- I viewed other gym and health websites to gain inspriation on what design fits best for this type of website. 
- I made sure my site was accessible by making sure all text is readable and that there is a right amount of contrast between colours. 
- I selected the colour pallet yellow, black and white as I thought it reflected strength and agility colours which would be assoicated with fitness and energy. These hard colours are strong and inviting but also smart and serious. 
- I made sure my site was simple as a design principle for an ease in terms of user experience. 
- I selected a simple readable, pleasing font to make sure my text was easily and quickly readable. 
- I provided ease of navigation so that the user can go back and forth between the homepage, browse merchandise, basket/checkout and profile. I also provided the ability for the user to have their own profile so that they can 
- I created a favicon icon with the intials of my site 'GG'. I used an eyecatching font and stuck with the pallet of my site.
- I created a wireframe of my project prior to creating it, this wireframe allowed me to have a simple basis of what I developing and how it should look. 

## Wireframe 

![wireframe](/media/PP4/wireframe.png) 

## Facebook Business Page

![Facebook-Mockup](/media/facebook.png) 

- I implemented a mock up of a Facebook business page. I attempted to create an account numerous times but it kept getting shut down due to Facebook security so in the end I created a mock up in Canva to envision what GymGeeks business page would look like. I placed the logo 'workout' stamp as the icon/slogan and implemented it on the image of Facebook posts. I implemented it as such to keep the flow of the page and my site, linking it with the 'workout' stamp. I thought if it was used and placed regularly it would make my site more marketable and recognizsable. I envision this page to be a hub for community amongst GymGeek users. For users to find gym offers, subscriptions, classes or active-wear deals.  

## Final Project

![final project](/media/PP4/Home.png) 

- As you can see my design basically stayed the same but with a better color pallet and navigation placed beside a nicer designed 'workout' stamp on the homepage. 
- I also provided a 'shop now' button template and short detail of the site along with examples of what the shop/basket would look like. 

# Deployment 

I took the following steps to begin my deployment:

1. I installed Django and the supporting libraries.
2. I created a new blank Django project and app.
3. I set my project to use Cloudinary (where my images would be stored) and PostgreSQL (relational database management system). 
4. Deployment came into difficulty when Heroku stopped offering free accounts and so I had apply for a student gitpod starter pack and export my older projects data to ElephantSQL. Luckily I had not deployed my PP5 by this point so I did not have to migrate my files to a new database. ElephantSQL was all hooked up before I began deployment.
5. I created an app named 'GymGeeks' and gave it the location - 'Europe.'
5. By following the steps outlines by Code Institute I added ElephantSQL as my database in the Resources tab of my app - I migrated my older data from Postgres to ElephantSQL. 
6. I copied the DATABASE_URL from my Config Vars and added it to my env.py file to link my new database_url with my Heroku app.
7. I created my SECRET_KEY in my environ.py file to encrypt session cookies and added this to my Heroku app config vars.
8. I then imported dj_database_url, os and added my SECRET_KEY and DATABASES to my settings.py file.
9. I migrated my files. 
10. I created a Cloudinary account to store my images- I linked this URL to my env.py file and my Heroku app config vars.
11. In my settings.py file I added 'cloudinary_storage' and the cloudinary library to my INSTALLED_APPS.
12. After linking Django to Cloundinary, adding my Templates Directory, creating my three directories - media, static and templates, adding a Procfile (web: gunicorn gymgeeks.wsgi) and adding my heroku app to ALLOWED_HOSTS in my settings.py file- I was then ready to make my first deployment to Heroku. 
13. In the deployment tab of my app I connected GitHub to my deployment method. 
14. I then connected my app to my GitHub repository and deployed it to my main branch. 
15. I watched the buliding log and when it was complete I selected 'open app' and my app successfully deployed. 
16. On final deployment I set "DEBUG = False". 

# Credits

- Thank you to friends and family for putting up with me through the last rounds of this diploma. 
- Thank you to my mentor for his guidance. 

