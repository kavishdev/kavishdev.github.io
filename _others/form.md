---
layout: index
title: Maths Game
---

## The simple math addition tool that I have made.

<h1>Enter the Answer as fast as you can</h1>
<h2>Question number : {{qnumber}}<br> The question is {{question}}</h2>
<form action="/check" method= "GET">
    <input type="hidden" id = "qnumber" name="qnumber" value="{{qnumber}}">
    <label for="answer">Enter The Answer : </label><br> 
    <input type="text" id="answer" name="answer"><br>
    <!-- <label for="lname">Last name:</label>--><br> 
    <!-- <input type="text" id="lname" name="lname"> -->
    <input type="submit" value="Submit" >
</form>