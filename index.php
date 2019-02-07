<!--
Author: Joshua Buist
Visum IO Monitoring Platform (c) 2019 - All Rights Reserved

-->

<?php 

$cssVersion = date("Y-m-d-H-i-s");

//TO-DO
//Turn into template based system linked to SQL
$panels = 4;
$panelNames = ['Server 1','Server 2','Server 3', 'Server 4'];
$panelHosts = [2,3,1,4];
$panelClients = [1,1,1,1];
$panelStatus = [91,92,100,99];

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    
    <title>ViSUM IO</title>

    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link rel="stylesheet" type="text/css" media="screen" href="css/reset.css?v=<?php echo ($cssVersion);?>" />
    <link rel="stylesheet" type="text/css" media="screen" href="css/fonts.css?v=<?php echo ($cssVersion);?>" />
    <link rel="stylesheet" type="text/css" media="screen" href="css/colors.css?v=<?php echo ($cssVersion);?>" />
    <link rel="stylesheet" type="text/css" media="screen" href="css/main.css?v=<?php echo ($cssVersion);?>" />
    
    <script src="js/main.js"></script>
</head>
<body>
    <header>
        <div class="logoContainer">
            <h1 class="logo">V<span class="logoI">&nbsp;i&nbsp;</span>SUM - Demo</h1>
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
        ?>
                    <div class="panel">
                        <div class="panelContent">
                            <h2 class=""><?php echo($panelNames[$i]);?>
        <?php


        ?>
                        </div>
                    </div>
        <?php
            }
        ?>

        </div>
    </main>

    <footer>

    </footer>
</body>
</html>