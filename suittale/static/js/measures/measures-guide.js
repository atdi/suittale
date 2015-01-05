/**
 * Created by aurel on 1/3/15.
 */
function getManSuitMeasures() {

    return {shoulders: '1',
                chest: '2',
                waist: '3',
                hips: '4',
                inside_leg: '5',
                external_leg: '6',
                coat_length: '7',
                sleeve: '8'
        };

}

function getManPantsMeasures() {

    return {    waist: '1',
                hips: '2',
                inside_leg: '3',
                external_leg: '4'
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

    this.drawPantsNumbers = function(size) {
        var pantsMeasures = getManPantsMeasures();
        if(size) {
            pantsMeasures = new MeasuresHandler().getByTypeAndSize('T1', size);
        }
        this.values = {
                waist: drawText(pantsMeasures.waist, new Point(260, 221)),
                hips: drawText(pantsMeasures.hips, new Point(260, 276)),
                insideLeg: drawText(pantsMeasures.inside_leg, new Point(260, 396)),
                externalLeg: drawText(pantsMeasures.external_leg, new Point(44, 396))
        };
    }

    this.drawSuitNumbers = function(size) {
        var suitMeasures = getManSuitMeasures();
        if(size) {
            suitMeasures = new MeasuresHandler().getByTypeAndSize('T1', size);
        }
        this.values = {shoulders: drawText(suitMeasures.shoulders, new Point(260, 114)),
                chest: drawText(suitMeasures.chest, new Point(260, 146)),
                waist: drawText(suitMeasures.waist, new Point(260, 221)),
                hips: drawText(suitMeasures.hips, new Point(260, 276)),
                insideLeg: drawText(suitMeasures.inside_leg, new Point(260, 396)),
                externalLeg: drawText(suitMeasures.external_leg, new Point(44, 396)),
                coatLength: drawText(suitMeasures.coat_length, new Point(44, 186)),
                sleeve: drawText(suitMeasures.sleeve, new Point(44, 136))
        };
    };

    this.deleteInitialNumbers = function() {
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

    this.drawPantsLines = function() {
        this.drawWaistLine();
        this.drawHipsLine();
        this.drawInsideLegLine();
        this.drawExternalLegLine();
        this.drawPantsNumbers();
    };
};

var path = window.location.pathname;
var measures = new MeasuresGraphics();

if(path == '/suitmeasures') {
    measures.drawSuitLines();
    $( "tr[name=suit_measure]" ).mouseenter(function() {
        measures.deleteInitialNumbers();
        measures.drawSuitNumbers($( this).attr('id'));
        view.draw();
    }).mouseleave(function() {
        measures.deleteInitialNumbers();
        measures.drawSuitNumbers();
        view.draw();
    });
}

if(path == '/pantsmeasures') {
    measures.drawPantsLines();
    $( "tr[name=pants_measure]" ).mouseenter(function() {
        measures.deleteInitialNumbers();
        measures.drawPantsNumbers($( this).attr('id'));
        view.draw();
    }).mouseleave(function() {
        measures.deleteInitialNumbers();
        measures.drawPantsNumbers();
        view.draw();
    });
}

