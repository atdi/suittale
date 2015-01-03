/**
 * Created by aurel on 12/29/14.
 */
function ProductsRender() {
    var url = '/api/products';
    var getProducts = $.ajax({
                          url: '/api/products',
                          dataType: 'json',
                          type: 'GET'
                        });
    var templatePath = "/static/templates/products/_productList.tmpl.html";
    var templateContent = $.get(templatePath);

    var renderProducts = function(templateContent, data) {
        this.products = new Ractive({
                          el: '#content',
                          template: templateContent,
                          data: { products: data }
                        });
    }

    var renderTemplate = function(data) {
        $.when(templateContent).done(function(templateContent) {
            renderProducts(templateContent, data);
        });
    }

    this.getProducts = function() {
        $.when(getProducts).done(function(data) {
            if (data != null && data.num_results > 0) {
                renderTemplate(data.objects);
            }
        });
    }
};

(new ProductsRender()).getProducts();
