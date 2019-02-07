<!--
Author: Joshua Buist
Luna Visum Monitoring Platform (c) 2019 - All Rights Reserved
Licensed to iUNU Inc. 2019
-->

{% load static %}
<?php 

$panels = 4;

echo "Hello World";

?>

<!Doctype <!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    
    <title>LUNA ViSUM</title>

    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link rel="stylesheet" type="text/css" media="screen" href="{% static 'view/css/reset.css' %}?v=1.06" />
    <link rel="stylesheet" type="text/css" media="screen" href="{% static 'view/css/fonts.css' %}?v=1.06" />
    <link rel="stylesheet" type="text/css" media="screen" href="{% static 'view/css/colors.css' %}?v=1.06" />
    <link rel="stylesheet" type="text/css" media="screen" href="{% static 'view/css/main.css' %}?v=1.06" />
    
    <script src="{% static 'view/js/main.js' %}"></script>
</head>
<body>
    <header>
        <div class="logoContainer">
            <h1 class="logo">LUNA ViSUM</h1>
        </div>
        <nav>   
            <a class="fas fa-bars"></a>
        </nav>
    </header>

    <main>
        <div class="vSpace"></div>
        
        <div class="container">


        <?php
         $array = array( 1, 2, 3, 4, 5);
         
         foreach( $array as $value ) {
            echo "Value is $value <br />";
         }
      ?>

        </div>
    </main>

    <footer>

    </footer>
</body>
</html>