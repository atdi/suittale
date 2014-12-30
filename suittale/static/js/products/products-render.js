/**
 * Created by aurel on 12/29/14.
 */

$.ajax({
      url: '/api/products',
      dataType: 'json',
      success: function(data) {
        console.log(data);
        var Products = new Ractive({
                          el: '#example',
                          template: '{{#products}}<div class="col-sm-6"><p>{{name}}</p><img src="/static/{{image}}" width="200" height="400"/></div>{{/products}}',
                          data: {products: data.objects}
                        });

      },
      error: function(xhr, status, err) {
        console.error('/api/products', status, err.toString());
      }
    });
