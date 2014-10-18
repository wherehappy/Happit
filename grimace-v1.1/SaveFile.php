<?php

$DIRNAME = 'uploads/';
$PREFIX = '';

$WATCHDOG = 100000;

if (!file_exists($DIRNAME)) {
	mkdir($DIRNAME);
}

// sense mime type of uploaded file for correct extension
$mime = $_SERVER['CONTENT_TYPE'];
switch ($mime) {
	case 'image/png':
		$filetype = 'png';
		break;
		
	case 'image/jpeg':
		$filetype = 'jpg';
		break;
		
	default: 
		echo "Supplied MIME type not allowed for upload.";
		exit(1);
}

// generate filename
do {
	$filename = md5(microtime());
	$uploadUrl = $DIRNAME . $PREFIX . $filename . '.' . $filetype;
}
while(file_exists($uploadUrl));

// handle upload
$postdata = fopen("php://input", "rb"); 
$fp = fopen($uploadUrl, 'wb');

while (!feof($postdata)) {
	fwrite($fp, fread($postdata, 4096));
}

fclose($fp);
fclose($postdata);


// generate absolute URL to uploaded file
$scriptDir = $_SERVER['SCRIPT_NAME'];
$scriptDir = substr($scriptDir,0,strripos($scriptDir,'/'));


printf("http://%s:%s/%s/%s", $_SERVER['SERVER_NAME'], $_SERVER['SERVER_PORT'], $scriptDir, $uploadUrl);
exit(0);




// courtesy of http://at2.php.net/manual/de/function.mkdir.php
/**
 * Makes directory and returns true if exists OR made.
 *
 * @param  $path Path name
 * @return bool
 */
function rmkdir($path, $mode = 0755) {
    $path = rtrim(preg_replace(array("/\\\\/", "/\/{2,}/"), "/", $path), "/");
    $e = explode("/", ltrim($path, "/"));
    if(substr($path, 0, 1) == "/") {
        $e[0] = "/".$e[0];
    }
    $c = count($e);
    $cp = $e[0];
    for($i = 1; $i < $c; $i++) {
        if(!is_dir($cp) && !@mkdir($cp, $mode)) {
            return false;
        }
        $cp .= "/".$e[$i];
    }
    return @mkdir($path, $mode);
}

?>