$(document).ready(function(){ // start

  $('body').keypress(function (e) {
   var key = e.which;
   if(key == 13)  // the enter key code
    {
      $('#search_title').click();
      return false;
    }
  });


  $("#search_title").click(function(){
    search_term = $("#book_title").val()
    $.ajax({
      type: 'get',
      url: 'https://www.googleapis.com/books/v1/volumes?q=' + search_term + '&key=AIzaSyA8zAFCmNbOcEjPZuAOdq2XcxcMBui8DLU',
      success: function(data){
        $(".content").html("")
        console.log(data.items)
        for (var i = 0; i < data.items.length; i++) {
          var authors = String(data.items[i].volumeInfo.authors).split(",").join(", ")
          if (data.items[i].volumeInfo.imageLinks === undefined) {
            var image = 'http://icdn.pro/images/en/b/r/broken-record-icone-5016-96.png'
          } else {
            var image = String(data.items[i].volumeInfo.imageLinks.thumbnail)
          }
          // needs regex
          var title = String(data.items[i].volumeInfo.title)
          var google_id = String(data.items[i].id)

          var bookRecord = {
            authors_i: authors,
            image_i: image,
            title_i: title,
            google_id_i: google_id
          };
          var bookTemplate = $('#bookTemplate').html();
          var compiledBookTemplate = _.template(bookTemplate);

          $('.content').append(compiledBookTemplate(bookRecord));

        }

      }, error: function() {
        console.log("It didn't work.");
      }
    })
})


}); // end document.ready
