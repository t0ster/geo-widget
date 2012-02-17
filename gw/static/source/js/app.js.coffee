$(document).ready ->
  $("[rel='autocomplete']").autocomplete({
      source: (request, response) ->
        data = {}
        data[$(this.element).attr("name")] = $(this.element).val()
        $.ajax(
          type: "GET",
          url: $(this.element).data("url"),
          data: data,
          dataType: "json",
          success: (data) ->
            response(data)
        )
  })
