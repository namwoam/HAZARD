var currentList = ["wind", "flood", "fire"]
var current = "wind"
var current_video = "1"


function Change(idx){
    var li_list = document.getElementById("scene-ul").children;
    console.log(idx);
    console.log(li_list);
    for(i = 0; i < li_list.length; i++){
        li_list[i].className = "";
    }
    li_list[idx].className = "active";
    current = currentList[idx]
    document.getElementById("scene_video").src = "video/" + current + "/" + current_video + '.mp4';
    
}

function ChangeScene(video_idx){
    var li_list = document.getElementById("scene-view-ul").children;
    console.log(video_idx);
    console.log(li_list);
    for(i = 0; i < li_list.length; i++){
        li_list[i].className = "";
    }
    li_list[video_idx-1].className = "active";
    current_video = video_idx.toString()
    document.getElementById("scene_video").src = "video/" + current + "/" + current_video + '.mp4';
}
