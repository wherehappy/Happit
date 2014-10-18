
EMOTION
EMOTION PHP 


<?php
//$file = './people.txt';
$file="/var/www/html/grimace-v1.1/demos/js/q.txt";
// The new person to add to the file
$person = "John Smith\n";
// Write the contents to the file, 
// using the FILE_APPEND flag to append the content to the end of the file
// and the LOCK_EX flag to prevent anyone else writing to the file at the same time
file_put_contents($file, $person, FILE_APPEND | LOCK_EX);
echo ' :)';

print_r(error_get_last(),true);
echo(error_get_last());

echo '<hr/>';
?>

<?php


/*
$message = "Test";
$myFile = "/var/www/html/grimace-v1.1/demos/js/testFile.txt";
if (file_exists($myFile)) {
  $fh = fopen($myFile, 'a');
  fwrite($fh, $message."\n");
} else {

//chmod("/path/to/dir/ *", 0755);
  $fh = fopen($myFile, 'w')  or die("Cannot open file \"$myFile\"...\n");
  fwrite($fh, $message) ;
}
fclose($fh);
*/


/*
echo 'a fear=' . htmlspecialchars($_GET["Xfear"]) . '!';
echo 'QUERY=' . $_GET . '';

echo '  ISSET=' . (isset($_GET['Xjoy']));

echo 'xx';
if (isset($_GET['Xjoy'])){
echo '+++';
}
*/




$myFile = "./recordsfile.txt";


//$myFile="/var/www/html/grimace-v1.1/demos/js/recs.txt";

echo '(' . $myFile . ')';

$fh = fopen($myFile, 'a');

//print_r(error_get_last(),true);

/*
echo '[' .$fh . '] file';
if($fh){
	fclose($fh);
echo '(closed.)';
}else{
echo 'FAILED OPENING FILE';

print_r(error_get_last(),true);
}
*/
/* or {echo ("can't open file");};
*/

if($fh){
//$stringData = 'EMOTIONS' . $_GET . "\n";

$stringData = 'EMOTIONS  ' . $_SERVER['QUERY_STRING'] . "\n";

fwrite($fh, $stringData);
//$stringData = "New Stuff 2\n";
//fwrite($fh, $stringData);
fclose($fh);




//echo '[' .$fh . '] file';
//if($fh){
//        fclose($fh);
echo '(closed.)';

}else{
echo 'FAILED OPENING FILE';

print_r(error_get_last(),true);
}

/*
X_joy='0';
if (isset($_GET["Xjoy"]))){
X_joy=htmlspecialchars($_GET["Xjoy"]) . '';
}

echo 'anyway JOY=' . X_joy;
*/
/*
return;
echo $_GET["Xjoy"]) . '';
echo '. ';
echo $_GET["Xsurprise"]) . '';
echo '. ';
echo $_GET["Xfear"]) . '';
echo '. ';
echo $_GET["Xsadness"]) . '';
echo '. ';
echo $_GET["Xdisgust"]) . '';
echo '. ';
echo $_GET["Xanger"]) . '';
echo '. ';

*/


//phpinfo();
?>


