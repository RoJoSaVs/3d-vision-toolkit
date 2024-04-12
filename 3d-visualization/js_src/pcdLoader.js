
import * as THREE from "three";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls.js";
import { PCDLoader } from "three/examples/jsm/loaders/PCDLoader.js";


var pcdFilePath = ''


// Configure the scene
var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
var renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);


// Configure controls of the camera
var controls = new OrbitControls(camera, renderer.domElement);
camera.position.z = 5;


// Configure the light
var ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
scene.add(ambientLight);
var directionalLight = new THREE.DirectionalLight(0xffffff, 0.5);
scene.add(directionalLight);


// Render the scene
function animate() {
    requestAnimationFrame(animate);
    controls.update();
    renderer.render(scene, camera);
}


function cleanScene() {
    while(scene.children.length > 0){ 
        scene.remove(scene.children[0]); 
    }
}


window.onload = function() {
    // Get reference to the input and the file
    var inputPCD = document.getElementById('fileInput');

    inputPCD.addEventListener('change', function(event) {
        // Check if a file was selected
        if (inputPCD.files && inputPCD.files[0]) {
            // Create a URL object for the selected pcd file
            var newPCDUrl = URL.createObjectURL(inputPCD.files[0]);
            
            // Assign the new image URL to the src of the pcd
            pcdFilePath = newPCDUrl;
            cleanScene();

            // Configure the loading file (pcd)
            var loader = new PCDLoader();
            loader.load(pcdFilePath, function (points) {
                scene.add(points);
            });

            animate();
            console.log("hello");
        }
    });
};