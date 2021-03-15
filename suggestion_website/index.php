<html>
    <head>
        <title>Dinner Suggestions</title>
    </head>

    <body>
        <h1>Here is a dinner suggestion</h1>
        <ul>
            <?php
                $json = file_get_contents('http://dinner-service/');
                $obj = json_decode($json);

                $dinner = $obj->dinner;
                echo "$dinner<br />";
            ?>
        </ul>
        <h4>Refresh the page for a different suggestion.</h2>
    </body>
</html>