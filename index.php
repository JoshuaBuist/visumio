<!--
Author: Joshua Buist
Visum IO Monitoring Platform (c) 2019 - All Rights Reserved

-->

<?php 

$panels = 4;

?>

<!Doctype <!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    
    <title>ViSUM IO</title>

    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link rel="stylesheet" type="text/css" media="screen" href="css/reset.css?v=1.06" />
    <link rel="stylesheet" type="text/css" media="screen" href="css/fonts.css?v=1.06" />
    <link rel="stylesheet" type="text/css" media="screen" href="css/colors.css?v=1.06" />
    <link rel="stylesheet" type="text/css" media="screen" href="css/main.css?v=1.06" />
    
    <script src="js/main.js"></script>
</head>
<body>
    <header>
        <div class="logoContainer">
            <h1 class="logo">ViSUM IO</h1>
        </div>
        <nav>   
            <a class="fas fa-bars"></a>
        </nav>
    </header>

    <main>
        <div class="vSpace"></div>
        
        <div class="container">


        <?php
            for ($i = 0; $i<$panels; $i++)
            {
                echo ("<div class='panel'><div class='panelContent'></div></div>");
            }
        ?>

        </div>
    </main>

    <footer>

    </footer>
</body>
</html>