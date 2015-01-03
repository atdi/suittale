/**
 * Created by aurel on 1/3/15.
 */
function getSuitMeasures(size) {
    if(size == 42) {
        return {shoulders: '42-43',
                chest: '96-97',
                waist: '75-78',
                hips: '92-94',
                insideLeg: '88',
                externalLeg: '109',
                coatLength: '76',
                sleeve: '63'
        };
    }

    if(size == 44) {
        return {shoulders: '44',
                chest: '98-99',
                waist: '79-82',
                hips: '95-97',
                insideLeg: '88',
                externalLeg: '110',
                coatLength: '76,5',
                sleeve: '63,5'
        };
    }

    return {shoulders: '1',
                chest: '2',
                waist: '3',
                hips: '4',
                insideLeg: '5',
                externalLeg: '6',
                coatLength: '7',
                sleeve: '8'
        };

}


/**
 *
 * @constructor
 */
function MeasuresGraphics() {

    var raster = new Raster('suit');
    raster.position = view.center;

    /**
     *
     * @param strokeColor
     * @param startPoint
     * @param x
     */
    var drawLine = function(strokeColor, startPoint, x,y) {
        var path = new Path();
        path.strokeColor = strokeColor;
        var start = startPoint
        path.moveTo(start);
        path.lineTo(start + [x, y]);
    };

    /**
     *
     * @param text
     * @param point
     */
    var drawText = function(text, point) {
        var pointText = new PointText(point);
        pointText.justification = 'center';
        pointText.fillColor = 'black';
        pointText.content = text;
        return pointText;
    };

    /**
     *
     */
    this.drawShouldersLine = function() {
        drawLine('#ffffff', new Point(104, 117), 118, 0);
        drawLine('#000000', new Point(222, 117), 40, 0);
    };

    /**
     *
     */
    this.drawChestLine = function() {
        drawLine('#ffffff', new Point(118, 150), 90, 0);
        drawLine('#000000', new Point(208, 150), 54, 0);
    };

    this.drawWaistLine = function() {
        drawLine('#ffffff', new Point(123, 225), 77, 0);
        drawLine('#000000', new Point(200, 225), 62, 0);
    };

    this.drawHipsLine = function() {
        drawLine('#ffffff', new Point(114, 280), 90, 0);
        drawLine('#000000', new Point(204, 280), 58, 0);
    };

    this.drawInsideLegLine = function() {
        drawLine('#ffffff', new Point(166, 299), 0, 179);
        drawLine('#000000', new Point(167, 400), 95, 0);
    };

    this.drawExternalLegLine = function() {
        drawLine('#ffffff', new Point(123, 226), 0, 250);
        drawLine('#000000', new Point(122, 400), -80, 0);
    };

    this.drawCoatLengthLine = function() {
        drawLine('#ffffff', new Point(152, 93), 0, 205);
        drawLine('#000000', new Point(149, 190), -107, 0);
    };

    this.drawSleeveLine = function () {
        drawLine('#ffffff', new Point(106, 112), -14, 162);
        drawLine('#000000', new Point(103, 140), -61, 0);
    };

    this.drawInitialSuitNumbers = function() {
        this.values = {shoulders: drawText('1', new Point(260, 114)),
                chest: drawText('2', new Point(260, 146)),
                waist: drawText('3', new Point(260, 221)),
                hips: drawText('4', new Point(260, 276)),
                insideLeg: drawText('5', new Point(260, 396)),
                externalLeg: drawText('6', new Point(44, 396)),
                coatLength: drawText('7', new Point(44, 186)),
                sleeve: drawText('8', new Point(44, 136))
        }
    };

    this.deleteInitialSuitNumbers = function() {
        for(var key in this.values){
            this.values[key].remove();
        }
        raster.refresh();
    }

    this.drawSuitLines = function() {
        this.drawShouldersLine();
        this.drawChestLine();
        this.drawWaistLine();
        this.drawHipsLine();
        this.drawInsideLegLine();
        this.drawExternalLegLine();
        this.drawCoatLengthLine();
        this.drawSleeveLine();
        this.drawInitialSuitNumbers();
    };
};

var measures = new MeasuresGraphics();
measures.drawSuitLines();

$( "a[name=measure]" ).click(function() {
  measures.deleteInitialSuitNumbers();

  alert( "Handler for .click() called." + $( this).attr('id'));
});