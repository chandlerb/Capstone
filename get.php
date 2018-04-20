<html>
    <h2>shit</h2>
<?php
$arr = file("mvp.txt");
for($line = 0; $line < count($arr); $line++)
    print(split($arr[$line], " "));
?>
</html>