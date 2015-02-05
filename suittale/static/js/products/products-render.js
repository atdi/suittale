/**
 * Created by aurel on 12/29/14.
 */


var ProductsRender = (function () {


    var url = null;
    var templatePath = null;
    var selector = null;

    function activateCarousel() {
        /* activate the carousel */
        $('#modalCarousel').carousel({interval: false});

        /* change modal title when slide changes */
        $('#modalCarousel').on('slid.bs.carousel', function () {
            $('.modal-title').html($(this).find('.active').attr("title"));
        });

        /* when clicking a thumbnail */
        $('.box .thumbnail').click(function () {
            var idx = $(this).parents('div').index();
            var id = parseInt(idx);
            $('#gallery-modal').modal('show'); // show the modal
            $('#modalCarousel').carousel(id); // slide carousel to selected

        });
    }

    function getProducts() {
        return $.ajax({
            url: url,
            dataType: 'json',
            type: 'GET'
            });
    }

    function templateContent() {
        return $.get(templatePath);
    }

    function renderProducts(templateContent, data) {
        new Ractive({
            el: selector,
            template: templateContent,
            data: {products: data}
        });
        if ($('#gallery-modal')) {
            activateCarousel();
        }

    };

    function renderProduct(templateContent, data) {
        new Ractive({
            el: selector,
            template: templateContent,
            data: data
        });
    };

    function renderListTemplate(data) {
        var content = templateContent();
        $.when(content).done(function (templateContent) {
            //window.history.pushState(data, 'Costume barbati', '/msuites');
            renderProducts(templateContent, data);
        }).fail(function(jqXHR, textStatus, errorThrown) {
            console.log.error(errorThrown);
        });
    }

    function renderTemplate(data) {
        var content = templateContent();
        $.when(content).done(function (templateContent) {
            //window.history.pushState(data, 'Costum barbat', '/msuites/'+data.id);
            renderProduct(templateContent, data);
        }).fail(function(jqXHR, textStatus, errorThrown) {
            console.log.error(errorThrown);
        });
    }

    function renderItems(iUrl, iTemplatePath, iSelector) {
        url = iUrl;
        templatePath = iTemplatePath;
        selector = iSelector;
        var products = getProducts();
        $.when(products).done(function (data) {
            if (data.objects != null) {
                renderListTemplate(data.objects);
            } else {
                renderTemplate(data);
            }
        }).fail(function(jqXHR, textStatus, errorThrown) {
            console.log.error(errorThrown);
        });
    }

    return {
        renderContent: renderItems
    };
})();


