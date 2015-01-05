/**
 * Created by aurel on 1/4/15.
 */

function MeasuresHandler() {
    var url = '/api/suit_size_guides';

    var search = function(filters) {
        var order_by = [{"field": "size", "direction": "asc"}]
        return $.ajax({
            type: "GET",
            url: url,
            data: {"q": JSON.stringify({"filters": filters, "order_by": order_by})},
            dataType: "json",
            contentType: "application/json",
            async: false
        }).responseText;
    }

    this.getByType = function(type) {
        var filters = [{"name": "type", "op": "==", "val": type}];
        var response = JSON.parse(search(filters));
        return response;
    }

    this.getByTypeAndSize = function(type, size) {
        var filters = [{"name": "type", "op": "==", "val": type},
        {"name": "size", "op": "==", "val": size}];
        var response = JSON.parse(search(filters));
        return response.objects[0];
    }
}

function MeasuresRender() {
    var templatePath = "/static/templates/measures/_suitMeasuresList.tmpl.html";
    var templateContent = $.get(templatePath);

    var renderProducts = function(templateContent, data) {
        this.measures = new Ractive({
                          el: '#measures_list',
                          template: templateContent,
                          data: { measures: data }
                        });
    }

    var renderTemplate = function(data) {
        $.when(templateContent).done(function(templateContent) {
            renderProducts(templateContent, data);
        });
    }

    this.getMeasures = function() {
        var data = new MeasuresHandler().getByType('T1');
        if (data != null && data.num_results > 0) {
            renderTemplate(data.objects);
        }

    }

};

(new MeasuresRender()).getMeasures();