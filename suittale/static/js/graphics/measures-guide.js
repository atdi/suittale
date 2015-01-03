/**
 * Created by aurel on 1/3/15.
 */

function MeasuresGraphics() {
    var raster = new Raster('suit');

    // Move the raster to the center of the view
    raster.position = view.center;


    var drawLine = function(strokeColor, startPoint, lenght) {
        var path = new Path();
        path.strokeColor = strokeColor;
        var start = startPoint
        path.moveTo(start);
        path.lineTo(start + [lenght, 0]);
    };

    this.drawShouldersLine = function() {
        drawLine('white', new Point(99, 117), 43);
        drawLine('black', new Point(142, 117), 17);
        drawLine('white', new Point(160, 117), 8);
        drawLine('black', new Point(168, 117), 19);
        drawLine('white', new Point(188, 117), 32);
        //path.lineTo(start + [ 121, 0 ]);
    }
};

var measures = new MeasuresGraphics();
measures.drawShouldersLine();

