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

    if(size == 46) {
        return {shoulders: '45',
                chest: '100-101',
                waist: '82-86',
                hips: '98-100',
                insideLeg: '88',
                externalLeg: '111',
                coatLength: '77',
                sleeve: '64'
        };
    }

    if(size == 48) {
        return {shoulders: '46',
                chest: '102-103',
                waist: '87-90',
                hips: '101-103',
                insideLeg: '89',
                externalLeg: '111',
                coatLength: '77,5',
                sleeve: '64,5'
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

    this.drawSuitNumbers = function(size) {
        var suitMeasures = getSuitMeasures(size);
        this.values = {shoulders: drawText(suitMeasures.shoulders, new Point(260, 114)),
                chest: drawText(suitMeasures.chest, new Point(260, 146)),
                waist: drawText(suitMeasures.waist, new Point(260, 221)),
                hips: drawText(suitMeasures.hips, new Point(260, 276)),
                insideLeg: drawText(suitMeasures.insideLeg, new Point(260, 396)),
                externalLeg: drawText(suitMeasures.externalLeg, new Point(44, 396)),
                coatLength: drawText(suitMeasures.coatLength, new Point(44, 186)),
                sleeve: drawText(suitMeasures.sleeve, new Point(44, 136))
        }
    };

    this.deleteInitialSuitNumbers = function() {
        for(var key in this.values){
            this.values[key].remove();
        }

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
        this.drawSuitNumbers();
    };
};

var measures = new MeasuresGraphics();
measures.drawSuitLines();

$( "a[name=measure]" ).mouseenter(function() {
    measures.deleteInitialSuitNumbers();
    measures.drawSuitNumbers($( this).attr('id'));
    view.draw();
}).mouseleave(function() {
    measures.deleteInitialSuitNumbers();
    measures.drawSuitNumbers();
    view.draw();
});