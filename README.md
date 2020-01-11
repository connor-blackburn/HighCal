# Milestone Project Four - Full Stack Frameworks With Django

[![Build Status](https://travis-ci.com/connorblackburn98/HighCal.svg?branch=master)](https://travis-ci.com/connorblackburn98/HighCal)

[Live Site](https://highcal-django.herokuapp.com/)

I have created a full stack, fully functioning website. It is based around the project theme of a web developers business website. The goal was a simple one; ensure the website can prove to be an effective hub for all business.

Want to start a job together? Buy any merchandise? See previous work? To read previous reviews for the products and previous clients? Read the recent business news or tips? The project makes the above (and much more) extremely achievable for any user visiting the site.

The full stack website was made possible written in the python-based web framework; Django. It provides a developer all the tools and equipment needed to create large functioning websites with ease and speed.

## UX 

For any project to be considered successful, it must cater for those who most need it. Understanding the target audience for the project was a must, but more importantly; I needed to understand why they would use the site and what problems they needed solving.

Before embarking on the project, I wrote down who exactly would be using the site and why. Along with several UX mockups which can be seen within the mockups directory of the project.

1. An individual or business interesting in becoming a client.

   * Given the nature of the web development industry; any potential client may hold the site as the only true way of gaining a full understanding of the company and its work. This will result in the site potentially being the sole way of new customers to find and work with the web developer. 

   * For this reason and to aid this target group; it was vital to ensure this website can prove to be an effective hub for all business-related activities. It holds the ability to contact the business, sell merchandise, provide news/tips within a blog section, hold and present client reviews and showcase with links to previous work.

2. An aspiring developer wanting to receive advice/tips and to see what is possible within the industry.

   * A new developer may use the site to gain experienced advice and tips to better themselves and to gain an understanding of realistic goals and what is achievable. Although this target group may not be directly linked with company sales and profit; it does not mean that this group is not important to cater to and aid however possible. 

   * For this reason, the project is given a contact form where a user can submit a short form and a direct email will be sent to the company, allowing users and the developer to communicate effectively. In addition to this, there is also a blog section where an admin with ‘superuser’ status can write blog posts containing content such as recent news and tips, then post them to the website where users can access and benefit from. Blog posts can also be searched for in relation the post title. The search bar is placed at the very top of the Blog section page.

   * The site also has a portfolio section which will present all previous work completed by the company along with a button linking to each live site. This gives the user an opportunity to not only look at a project, but fully immerse themselves and explore the websites created. 

   * Any aspiring developer can gain a great amount of knowledge from the project which can be great for the community.

3. An individual wanting to show appreciation or voice an opinion.

   * Completing a successful job for a client is great, but if they cannot give you a review for all to see; it is a huge missed opportunity. A business can gain many new clients from simply showcasing previous client’s happiness.

   * Authenticated users within the site can create and post reviews directly to the website. These reviews will be displayed within the reviews section (accessed via the navigation bar). A snippet of the reviews will be presented with an expand button where interested individuals can go to a dedicated page and view the full review directly. 

   * Users can also give reviews ‘upvotes’. These can be used to take advantage of the review sorting functionality. A user can sort reviews based on highest votes, lowest votes, oldest and newest reviews, benefiting user experience.

4. A happy customer who may want to show further appreciation.

   * Understanding customers may want to show further appreciation to the business. I have created both a reviews section (explained above), and a merchandise store. This will give authenticated users the ability the either write a positive review for all to see or purchase a product from the merchandise store. Products can be searched for using the search bar placed at the top of the store page, the search will be related to the product name.
   
5. An individual wanting to contact the company.

   * Placed at the very top of the homepage, is a button labelled ‘Contact Us’, this directs the user to a short form which when completed will send the company an email with all the information about the sender and the ability to reply. This results in an effective means for communication to which highly benefits all parties involved.

## User Stories

Below I have listed the user stories I wrote before embarking on the project. It provided a great starting point to which I could start to form the site.

1. As a new user interested in work opportunities; I want to be able to see previous work from the company, any recent updates and a way to contact the company directly so I can act if needed.

   * For this reason, the users can complete a contact form which will send the company an email directly, a blog section keeping users up to date with news and tips, and a portfolio section so a user can view all previous work from the company, along with a live link to all sites so they can go and explore live, working versions of the work. 

2. As a previous client/customer, I want a way to review what I purchased so it can aid any new potential clients/individuals.

   * The review section of the website lists all previously written reviews from clients along with the ability to give reviews upvotes. A user can also sort the reviews based on highest or lowest votes, along with newest and oldest written reviews. Authenticated users can create and post reviews on the website for all the see.

3. As a user, I want to be able to create my own account so I will be able to purchase any merchandise and write reviews.

   * Users will be given the opportunity to register an account and log in whenever they want. The project provides full authentication features. They will gain several benefits to this, such as purchase products from the merchandise store and write reviews.

4. As a potential client and new user, I want to be able to see any new company updates quickly and contact the business with any questions I may have so it can help my decision making.

   * The blog section of the website proves a perfect place for a user to gain access to company updated, tips and general posts with the ability to search posts in relation to a post title to aid user experience. Users can also take advantage of the contact section of the project to send the company emails directly and to open the opportunity of communication.

5. As a potential client and new user, I want to easily be able to access previous work examples so I can see what my potential new website may look like.

   * The portfolio section of the website will showcase previous work in a clean manner, with a simple link with will direct the users within a new tab to the live working website they have chosen. Providing the perfect opportunity to explore previous work. 

## Features 

1. Full authentication capabilities.
   * A user has the ability the register an account, log in and log out. A user will be shown certain content and be given different abilities depending on their authentication status.

2. Main responsiuve navigation menu.
   * A responsive navigation menu provides the perfect hub for getting from A-to-B within the website. All areas of the website can be accessed throughout the navigation.

3. Blog section showing all posts.
   * A blog section will showcase any recent posts or updates in a shortened manner so a user can browse quickly and easily. An admin with superuser status can create and post updates to the website. A user can search for posts relevant to the post title, with the search bar placed within the blog section page.

4. Expanded post page for full viewing of specific post.
   * Once a user has found a desired post, a button will direct them to a blog detail page which will render the full blog post and all relevant details. 

5. Review section showing all reviews.
   * The review sections, like the blog section will render all reviews with shortened content so the user can browse quickly and easily. A user can sort reviews in relation to upvotes and oldest / newest reviews.

6. Expanded review section showing full review.
   * Once a desired review is found a button will lead a user to a dedicated page where the full review is rendered along with the ability to upvote the review.

7. Ability for authenticated users to write a review to post on site.
   * Authenticated users have the ability the write their own reviews and post them to the site. Users are told this when visiting the reviews page.

8. Merchandise section listing all products.
   * The merchandise store section lists all products available to user. A use can also search for relevant products with a search bar placed at the top of the page. 

9. Cart and checkout functionality.
   * Allows authenticated users to purchase products. Users are made aware of this when visiting merchandise store.

10. Responsive and clean design.
    * Responsive design means the whole site looks good and provides a positive user experience on all screen sizes and devices.

11.	Portfolio Page showing previous work with link to live site.
    * The portfolio section showcases all previous work with a button linking a user to the working live site so they can fully understand and experience the work quality of the company.

12. Contact functionality.
    * A user can fill out of the contact form which sends the company an email directly and will start communication between potential client and business.

## Future Feature Ideas

1. Comment section for blog posts.
   * I believe a comment section for blog posts will be an effective future feature for the project. Allowing the users to communicate more efficiently.

## Technologies Used

1. [HTML](https://en.wikipedia.org/wiki/HTML)
   * Providing the structure and core content to the project.

2. [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
   * Gives styling and responsiveness to the project.

3. [Bootstrap](https://getbootstrap.com/)
   * An open framework which aided development and responsive design.

4. [Django](https://www.djangoproject.com/)
   * Python web framework which the project is based around. Gives the project all its capabilities.

5. [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
   * Used to create the typewriter effect and to aid bootstrap elements.

6. [Heroku](https://dashboard.heroku.com/)
   * Used to deploy the python project to a live app.

7. [Github](https://github.com/)
   * Platform used to push each commit and keep a structured online repository.

## Deployment

The deployment process started within my online IDE; ‘Gitpod’. IT was this platform in which I wrote all the code during the development process. 

Once I was happy with a minor milestone within the project, I then pushed my code at that time to my online GitHub repository. This ensures the code is saved and is pushed online linked with a relevant commit message explaining what is new for that version of code.

As the project is python based, I needed to take advantage of Heroku to allow me to deploy the live version of the project so users can experience a live, working app. To do this, I was required to create a requirements.txt and a Procfile which tells Heroku which packages to install to help create and run the project correctly. To aid static file hosting I was also required to install and configure whitenoise. The final thing I needed to do in order to cater to Heroku deployment was to migrate my sql database to a postgres database offered by Heroku.

## Testing

Along with the automatic Travis testing (outcome placed at top of file), manual testing took place throughout the project to ensure its overall efficiency was positive. These tests are listed below and will be proven to be successful throughout the live app.

1. Users can successfully create a new account.
2. Users can then log into the new account using either the username or email along with password.
3. Users can log out and complete all authentication methods.
4. All buttons and links throughout the site direct to the correct pages.
5. Main navigation points to every area of the site successfully.
6. Authenticated user can add products to cart and purchase a product successfully using test card credentials.
   * Card test details
   * Card Number : 4242 4242 4242 4242
   * Security Code (CSV): 111
   * Month / Year: Any Acceptable Expiry Date.
7. The project remains responsive and consistent regardless of device size.
8. Reviews can be submitted and posted to the site by authenticated users.
9. Users can search for products based on product title.
10. Users can search for blog posts based on post title.
11. Users can filter reviews based on upvotes and creation date.
12. user can apply upvotes to reviews.
13. Users can complete contact form which sends an email successfully with all relevant details.
14. Forms cannot be submitted with required fields left empty.

## Credits

### Media
   * Business Hero Image by [ISOMETRIC](https://isometric.online/) is licensed under [MIT License](https://isometric.online/license/)
   * Merchandise and Blog images by [Pexels](https://www.pexels.com/) under the [Pexels License](https://www.pexels.com/photo-license/)
