var DropzoneExample = function () {
    var DropzoneDemos = function () {
        
        console.log("asd121233qqq")
        Dropzone.options["f-importer"] = {
            paramName: "file",
            maxFiles: 1,
            maxFilesize: 1,
            // accept: function(file, done) {
            //     if (file.name == "justinbieber.jpg") {
            //         done("Naha, you don't.");
            //     } else {
            //         done();
            //     }
            // }
            init: function() {
                this.on("success", function(file) {

                    // myDropzone.on("success", function(response) {
            $("#m-importer").modal("hide")
            swal({
                title: "Importar Archivo",
                text: "datos cargados correctamente",
                icon: "success",
                buttons: {
                    cancel: {
                        visible: false,
                    },
                    confirm: {
                        text: "Aceptar",
                        value: true,
                        closeModal: true
                    }
                }
            })
        // });

                });
            }
        };

        // this.on("complete", function(file) {
        //     /* Maybe display some more file information on your page */
        //     console.log("complete")
        // });

        // Dropzone.on("success", function(file) {
        //     /* Maybe display some more file information on your page */
        //     console.log("success")
        // });
        // Dropzone.options.multiFileUpload = {
        //     paramName: "file",
        //     maxFiles: 10,
        //     maxFilesize: 10,
        //     accept: function(file, done) {
        //         if (file.name == "justinbieber.jpg") {
        //             done("Naha, you don't.");
        //         } else {
        //             done();
        //         }
        //     }
        // };
        // Dropzone.options.fileTypeValidation = {
        //     paramName: "file",
        //     maxFiles: 10,
        //     maxFilesize: 10, 
        //     acceptedFiles: "image/*,application/pdf,.psd",
        //     accept: function(file, done) {
        //         if (file.name == "justinbieber.jpg") {
        //             done("Naha, you don't.");
        //         } else {
        //             done();
        //         }
        //     }
        // };
    }
    return {
        init: function() {
            DropzoneDemos();
        }
    };
}();
DropzoneExample.init();