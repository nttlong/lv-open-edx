function ScormStudioXBlock(runtime, element) {

  var handlerUrl = runtime.handlerUrl(element, 'studio_submit');
  var fileUploadUrl = runtime.handlerUrl(element, 'file_upload_handler');
  var pollingParams = {id: null, interval: 5000, url: runtime.handlerUrl(element, 'upload_status')};

  function log(msg){
    console.log(msg);
  }

  function updateProgressUI(step, percentVal) {
    if(step)
        $(element).find('.current-step').text(step);
    $(element).find('.progress-container .bar').css({width: percentVal});
    $(element).find('.status-container .progress-percent').text(percentVal);
  }
  
  function pollUploadStatus() {
    $.getJSON(pollingParams.url, function(data) {
      var percentVal = data.progress + '%';
      updateProgressUI('Unpack and Storing', percentVal);

      if(percentVal == '100%'){
        clearInterval(pollingParams.id);
        $(element).find('.status-container .success-msg').text('Scorm package has been succesfully uploaded!');
      }else{
        pollingParams.id = setTimeout(pollUploadStatus, pollingParams.interval);
      }
    });
  }
  
  $(element).find('#scorm-file-select').bind('click', function(e) {
    e.preventDefault();
    $('#scorm_file').click();
  });

  $(element).find('#scorm_file').fileupload({
    dataType: 'json',
    type: 'POST',
    maxChunkSize: 20 * 1000000, // 20 MB
    autoUpload: false,
    url: fileUploadUrl,
    add: function(e, data) {
      var file = data.files[0];

      $(element).find('#scorm-file-select').hide();
      $(element).find('.file-chosen').text('File Chosen: ' + file.name);
      $(element).find('.status-container').show();

      data.submit().complete(function(result, textStatus, xhr) {
          if(result.status == 'error'){
            alert('Error while uploading scorm package: ' + result.message);

            $(element).find('.file-chosen').text('');
            $(element).find('#scorm-file-select').show();
            $(element).find('.status-container').hide();
          }
      });

    },
    progressall: function(e, data) {
      var percentInt = data.loaded / data.total * 100,
                    percentVal = parseInt(percentInt, 10) + '%',
                    doneAt=95;

      updateProgressUI('Uploading', percentVal);

      if(percentInt >= doneAt){
        pollingParams.id = setTimeout(pollUploadStatus, 3000);
      }
    }
  });

  $(element).find('.save-button').bind('click', function() {
    var form_data = new FormData();
    var file_data = $(element).find('#scorm_file').prop('files')[0];
    var display_name = $(element).find('input[name=display_name]').val();
    var description = $(element).find('textarea[name=description]').val();
    var weight = $(element).find('input[name=weight]').val();
    var display_width = $(element).find('input[name=display_width]').val();
    var display_height = $(element).find('input[name=display_height]').val();
    var display_type = $(element).find('input[name=display_type]:checked').val();
    var scorm_player = $(element).find('select[name=scorm_player]').val();
    var encoding = $(element).find('select[name=encoding]').val();
    var player_configuration = $(element).find('textarea[name=player_configuration]').val();
    form_data.append('file', file_data);
    form_data.append('display_name', display_name);
    form_data.append('description', description);
    form_data.append('display_width', display_width);
    form_data.append('display_height', display_height);
    form_data.append('weight', weight);
    form_data.append('display_type', display_type);
    form_data.append('scorm_player', scorm_player);
    form_data.append('encoding', encoding);
    form_data.append('player_configuration', player_configuration);
    runtime.notify('save', {state: 'start'});

    $.ajax({
      url: handlerUrl,
      dataType: 'text',
      cache: false,
      contentType: false,
      processData: false,
      data: form_data,
      type: "POST",
      success: function(response){
        runtime.notify('save', {state: 'end'});
      }
    });

  });

  $(element).find('.cancel-button').bind('click', function() {
    runtime.notify('cancel', {});
  });

}
