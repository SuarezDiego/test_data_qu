var DropzoneExample = function () {
    var DropzoneDemos = function () {
        // single file upload
        Dropzone.options["f-importer"] = {
            paramName: "file", // The name that will be used to transfer the file
            maxFiles: 1,
            maxFilesize: 1, // MB
            // accept: function(file, done) {
            //     if (file.name == "unive.jpg") {
            //         done("Naha, you don't.");
            //     } else {
            //         done();
            //     }
            // }
        };

        Dropzone.on("complete", function(file) {
            /* Maybe display some more file information on your page */
            console.log("complete")
        });

        Dropzone.on("success", function(file) {
            /* Maybe display some more file information on your page */
            console.log("success")
        });
        // // multi file upload
        // Dropzone.options.multiFileUpload = {
        //     paramName: "file", // The name that will be used to transfer the file
        //     maxFiles: 10,
        //     maxFilesize: 10, // MB
        //     accept: function(file, done) {
        //         if (file.name == "unive.jpg") {
        //             done("Naha, you don't.");
        //         } else {
        //             done();
        //         }
        //     }
        // };
        // // file type validation
        // Dropzone.options.fileTypeValidation = {
        //     paramName: "file", // The name that will be used to transfer the file
        //     maxFiles: 10,
        //     maxFilesize: 10, // MB
        //     acceptedFiles: "image/*,application/pdf,.psd",
        //     accept: function(file, done) {
        //         if (file.name == "unive.jpg") {
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