<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Capstone</title>
</head>
<body >
<div id="toChange" onload="run()">
</div>

<?php
$arr = file("MVP.txt");
for($line = 0; $line < count($arr); $line++)
    echo($arr[$line] . "<br>" );
?>
    

            
</script>    
</body>
</html>

