function toggleExtra() {
    const extra = document.getElementById('extraContent');
    const style = window.getComputedStyle(extra);

    if (style.display === 'none') {
    extra.style.display = 'block';
    } else {
    extra.style.display = 'none';
    }
    }

    function hover(){
    document.getElementById("img").src = "https://www.visitutah.com/azure/cmsroot/visitutah/media/site-assets/three-season-photography/southwestern-utah/southwestern-4/springdale_zion-national-park_dash-jay.jpg"
    }

    function leave(){
    document.getElementById("img").src = "https://www.nps.gov/zion/learn/nature/images/Big-Bend-11222021.jpg"
    }