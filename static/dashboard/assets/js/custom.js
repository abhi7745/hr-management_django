/**
 *
 * You can write your JS code here, DO NOT touch the default style file
 * because it will make it harder for you to update.
 * 
 */

"use strict";

function toast(title,message="",type="info",position="topRight"){
    let types=["info","question","success","error","warning"]
    if(types.includes(type)){
        iziToast[type]({
            title: title,
            message: message,
            position: position
        });
    }
}
