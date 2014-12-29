/**
 * Created by aurel on 12/29/14.
 */
var ProductList = React.createClass({
  render: function() {
    var productNodes = this.props.data.map(function (product) {
      return (
        <Product name={product.name}>
          {product.short_description}
        </Product>
      );
    });
    return (
      <div className="productList">
        {productNodes}
      </div>
    );
  }
});

var ProductBox = React.createClass({
  loadProductsFromServer: function() {
    $.ajax({
      url: this.props.url,
      dataType: 'json',
      success: function(data) {
        this.setState({data: data});
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
  },
  getInitialState: function() {
    return {data: []};
  },
  componentDidMount: function() {
    this.loadProductsFromServer();
  },
  render: function() {
    return (
      <div className="productBox">
        <ProductList data={this.state.data} />
      </div>
    );
  }
});

React.render(
            <ProductBox url="/api/products" />,
            document.getElementById('example')
);
