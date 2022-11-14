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

 - I had 22 User Stories in total and moved them in accordance with whether they were in progress or completed. Here are my User Stories:

           - As a Shopper I want the ability to book a class on the site so that I can make sure to get my slot and see what timetable classes are available on a weekly basis

           - As a Shopper I want the ability to read about GymGeek staff so that I can get a feel for who GymGeek are and what they offer

           - As a Shopper I want the ability to purchase a subscription to gym classes/membership so that I can easily sign up to GymGeek classes or membership

           - As a Admin I want the ability to easily delete/edit products* so that I can easily set up my site

           - As a Shopper I want the ability to easily select the quantity* so that I can ensure I don't accidentally select the wrong quantity

           - As a Shopper I want the ability to easily select the size* so that I can ensure I don't accidentally select the wrong product size

           - As a Shopper I want the ability to Easily see what I have searched for and the number of results so that I can quickly decide whether the product I want is available

           - As a Shopper I want the ability to Search for a product by name or description so that I can find a specific product I'd like to purchase

           - As a *site owner*  I want to be able to *login & see my schedule & clients so that everything is organised and readable* (could-have/future feature)

           - As a *site owner* I want my *booking system to be adjustable and follow my schedule/diary so that it is organised with accordance to my schedule* (could-have/future feature)

           - As a *site owner*  I want to be able to *receive bookings and make sure there are no double bookings so that I can set up meetings with my users* (could-have/future feature)

           - As a *site owner*  I want to be able to *vet comments before posting so that abusive/poor comments aren't posted.* (must-have/completed)

           - As a *site owner*  I want to be able to *post to my blog so that my users can engage and read my content* (must-have/completed)

           - As a *User* I want the ability to sign in/out so that I can *have access to the full features of the site* (must-have/completed)

           - As a *User* I want the ability to sign in/out via Facebook so that I can *streamline my account* (could-have/completed)

           - As a *User* I want the ability to *book an appointment with a nutritionist so that I can get help & advice with my health issues* (could-have/future feature)

           - As a *User* I want the ability to *read blogs so that I can learn about nutrition & health* (must-have/completed)

           - As a *User* I want the ability to *like posts so that I can engage with others* (should-have/completed)
           
           - As a *User*, I want the ability to *comment and delete and edit posts so that manage my own content* (must-have/completed)

 - I labelled them with MoSCow prioritization so that this allowed me to prioritise certain tasks to implement over less important tasks depending on time and scope. 
