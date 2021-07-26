<html>
    <body>
        <pre>
            <?php
                $my_file = fopen("index.php","r") or die ("Unable to open file!");
                echo fread($my_file, filesize("index.php"));
                fclose($my_file);
            ?>
        </pre>
    </body>
</html> 