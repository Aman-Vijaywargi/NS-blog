# NS Frontend 

## Intro to web development with HTML

### Getting Started

Hint: Create a div tag with the id name as text and then write the entire text mention within the quotations without any full shops or spaces
```HTML
<div id="text">Welcome to the world of Web development</div>
```

### Why Software

Hint: For h1 tag copy the entire given text in the quotation except the space at end and for paragraph write whatever you want
```HTML
<h1>Why I want to become a developer?</h1>
<p>The reason is software development can help you in building an app which can help you to lower your task which generally a person feel lasy to do that work.</p>
```

### Shopping or Holiday

Hint: Here main understanding is when it ask for ordered list, then create li list consisting data-ns-test attribute as shoppingList same you need to do the same for unordered list where the li list consisting data-ns-test attribute as holidayList
```HTML
<li data-ns-test="shoppingList">Mobile Phone</li> <*-- Ex for ordered list -->
<li data-ns-test="holidayList">Manali</li> <*-- Ex for unordered list -->
```

### Favorite Song

Hint: Create a div tag and in that div tag create an anchor tag with the name you are going to link it
```HTML
<div>My favourite song is <a href="https://www.youtube.com/embed/eNvUS-6PTbs">Cheri Cheri Lady</a></div>
```

### Favourite Animal

Hint: This is simple. Just use img tag with src and alt as attribute and then copy/paste the complete url in the src
```HTML
<img src="https://i.guim.co.uk/img/media/fe1e34da640c5c56ed16f76ce6f994fa9343d09d/0_174_3408_2046/master/3408.jpg?width=445&quality=45&auto=format&fit=max&dpr=2&s=c4f4d4981ad8e828c7d2402a47ed4f4f" alt="A Pug">
```

### Dog Adoption

Hint: Follow the procedure of unordered list and then follow the hierarchy like first start with anchor tag, use the img tag and then end the anchor tag
```HTML
<li><a href="https://en.wikipedia.org/wiki/Golden_Retriever">Golden Retriever<img src="https://upload.wikimedia.org/wikipedia/commons/c/cf/BassetHound_profil.jpg"></a></li>
```

### Block or Inline

Hint: Complete the entire code by following the sample code given in the question. In the "data-ns-test" attribute you need to give value as block-inline-*. Here * represents testcases you wanna check
```HTML
<div data-ns-test="block-inline-sup">
    <sup>Test1</sup>
    <sup>Test2</sup>
    Answer: Inline
</div>
```

## HTML Continues

### Myntra: Size Chart

Hint: You need to use <thead> for the heading and enter the heading part and use <tbody> for the remaining columns and you don't need to use <tbody> 3 times for different rows

### Myntra: Dog Adoption Application

Hint: Just follow the instructions as it is mentioned in the description of the problem. For form, use id="form" and for checkbox, follow as mentioned below
```HTML
<input id="name" type="text" placeholder="Name">
<input id="checkbox" type="checkbox" value='Have you ever lived with a Dog before?'>
<select id="multiSelect">
    <option value="Golden Retriver">Golden Retriver</option> 
    <option value="Husky">Husky</option> 
    <option value="Pug">Pug</option>    
</select>
```

### Semantic IMDb

Hint: You just need to use the HTML5 tags like header, nav, section aside, summary and footer. In those tags you can write anything you like and u need to mention proper ids to the given tags.
```HTML
<nav>
    <a id="nav-actor" href="#actor">Actor</a>
    <a id="nav-quote" href="#quote">Quote</a>
</nav>
<section id="quote">
    Kaabil kano kamiyabi jhak marke aaegi
</section>
```
