SUBMITTED <?php
//$file="/var/www/html/grimace-v1.1/demos/js/q.txt";
//$person = "John Smith\n";
//file_put_contents($file, $person, FILE_APPEND | LOCK_EX);
//echo ' :)';
//print_r(error_get_last(),true);
//echo(error_get_last());


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
//echo '(' . $myFile . ')';

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
echo 'SUCCESS.';
}else{
echo 'FAILED OPENING FILE';
//print_r(error_get_last(),true);
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
