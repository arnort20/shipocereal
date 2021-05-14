$(document).ready(function() {
    $('.sort_filter').on(  'change',  function(e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        $.ajax( {
            url: '/product?search_filter=' + searchText,
            type: 'GET',
            success: function(resp) {
                var newHtml = resp.data.map(d =>{
                return `<div class="well product">
                            <a href="static/productPictures" ${d.id}>
                            <img href="product-img" src="${d.firstimage}"/>
                            <h4>${d.name}</h4>
                            <p>${d.description}</p>
                            </a>
                        </div>`

                });
                $('products').html(newHtml.join(''));
                $('#search-box').val('')
            },
            error: function(xhr, status, error){
                //TODO:Show toastr
                console:error(error)
            }
        })
    });
});