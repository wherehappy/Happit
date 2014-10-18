// You can compile this demo like this:
// mxmlc -use-network=false -static-link-runtime-shared-libraries Demo.as
// Make sure the mxmlc executable is included in your PATH

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

	[SWF( width="500", height="450")]
	public class Demo extends Sprite {
		private var grimace:*;

		[Embed(source="../../bin/grimace.swf", mimeType="application/octet-stream")]
		private var grimaceClass:Class;
		
		public function Demo() {
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
			
			buildUI();
		}
		
		private function buildUI():void {
			var pos:int = 1;
			
			var set1Btn:Sprite = createButton('set 1');
            addChild(set1Btn);
			set1Btn.addEventListener(MouseEvent.CLICK, function():void {
		 		grimace.api.setEmotion({anger:1.0, surprise:0.5}, 0.2);
			});
			set1Btn.y = 30 * pos++;

			var set2Btn:Sprite = createButton('set 2');
            addChild(set2Btn);
			set2Btn.addEventListener(MouseEvent.CLICK, function():void {
		 		grimace.api.setEmotion({joy:1.0, disgust:0.5}, 0.2);
			});
			set2Btn.y = 30 * pos++;

			var resetBtn:Sprite = createButton('reset');
            addChild(resetBtn);
			resetBtn.addEventListener(MouseEvent.CLICK, function():void {
		 		grimace.api.resetEmotion(0.2);
			});
			resetBtn.y = 30 * pos++;

			var captureBtn:Sprite = createButton('capture');
            addChild(captureBtn);
			captureBtn.addEventListener(MouseEvent.CLICK, function():void {
		 		grimace.api.capture();
			});
			captureBtn.y = 30 * pos++;

		}
		
		private function createButton(label:String):Sprite {
            var sendBtn:Sprite = new Sprite();
            sendBtn.x = 380;
            var sendLbl:TextField = new TextField();
            sendLbl.x = 1;
            sendLbl.y = 1;
            sendLbl.selectable = false;
            sendLbl.autoSize = TextFieldAutoSize.LEFT;
            sendLbl.text = label;
            sendBtn.addChild(sendLbl);
            sendBtn.graphics.lineStyle(1);
            sendBtn.graphics.beginFill(0xcccccc);
            sendBtn.graphics.drawRoundRect(0, 0, (sendLbl.width + 2), (sendLbl.height + 2), 5, 5);
            sendBtn.graphics.endFill();
			return sendBtn;
		}
	}
}