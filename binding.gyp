{
  "targets": [
    {
      "target_name": "addon",
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "conditions":[
        ["OS=='win'", {
      	  "sources": [ "lib/windows.cc" ]
      	}],
        ["OS=='mac'", {
      	  "sources": [ "lib/macos.mm" ],
          "libraries": [ '-framework AppKit', '-framework ApplicationServices' ],
          "xcode_settings": {
            "GCC_ENABLE_CPP_EXCEPTIONS": "YES"
          }
      	}]
      ],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")"
      ],
      'defines': [ 'NAPI_CPP_EXCEPTIONS' ]
    }
  ]
}
