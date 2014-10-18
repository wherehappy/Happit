package {
	import flash.display.Sprite;
	import flash.display.Loader;
	import flash.text.TextField;
    import flash.text.TextFieldType;
    import flash.text.TextFieldAutoSize;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.utils.ByteArray;
	import flash.system.ApplicationDomain;
	import flash.system.LoaderContext;

	public class Embed extends Sprite {
		public var grimace:*;

		[Embed(source="../../bin/Grimace.swf", mimeType="application/octet-stream")]
		private var grimaceClass:Class;
		
		public function Embed() {
			var grimaceBytes:ByteArray = (new grimaceClass() as ByteArray);
			var ldr:Loader = new Loader();
			ldr.loadBytes(grimaceBytes, new LoaderContext(false, ApplicationDomain.currentDomain));
			var scope:* = this;
			ldr.contentLoaderInfo.addEventListener(Event.COMPLETE, function():void {
				scope.init(ldr.content);
			});
		}
		
		public function init(grimace:*):void {
			this.grimace = grimace;
			addChild(grimace);
			
			grimace.events.addEventListener('loadComplete', function(e:Event):void {
				grimace.api.setMaxBounds(300, 0);
				grimace.api.setPosition(40,20);
				grimace.api.draw();
			});
			
			grimace.api.setCaptureUrl('http://localhost:8888/grimacecapture/SaveFile.php');
			
			grimace.events.addEventListener('captureComplete', function(e:*):void {
				trace(e.url);
			});
			
			grimace.api.loadFacedata(new Array(
				'head.xml',
				'features.xml',
				'wrinkles.xml',
				'emotions.xml',
				'overlays.xml'
			), '../../meta/');
			
		}
	}
}