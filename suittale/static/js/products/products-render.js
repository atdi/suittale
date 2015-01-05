/**
 * Created by aurel on 12/29/14.
 */

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

function ProductsRender(url, templatePath) {
    var getProducts = $.ajax({
        url: url,
        dataType: 'json',
        type: 'GET'
    });

    var templateContent = $.get(templatePath);

    var renderProducts = function (templateContent, data) {
        new Ractive({
            el: '#content',
            template: templateContent,
            data: {products: data}
        });
        if ($('#gallery-modal')) {
            activateCarousel();
        }

    }

    var renderTemplate = function (data) {
        $.when(templateContent).done(function (templateContent) {
            renderProducts(templateContent, data);
        });
    }

    this.renderItems = function () {
        $.when(getProducts).done(function (data) {
            if (data != null && data.num_results > 0) {
                renderTemplate(data.objects);
            }
        });
    }
};


