<template>
    <div class="card">
        <div class="circle"></div>
        <div class="circle"></div>
        <div class="card-inner">
            <slot></slot>
        </div>
    </div>
</template>
<script lang="ts">
export default {
    name: 'transparent-plate-circle'
}
</script>
<style scoped>
.card {
	width: 300px;
	height: 400px;
	transition: all 0.2s;
	position: relative;
	background: transparent;
	cursor: pointer;
}

.card-inner {
	width: inherit;
	height: inherit;
	background: rgba(255,255,255,.05);
	box-shadow: 0 0 10px rgba(0,0,0,0.25);

	backdrop-filter: blur( 10px );
	-webkit-backdrop-filter: blur( 10px );
	border-radius: 8px;
	transition: all .5s;
}

.card:hover .card-inner {
	backdrop-filter: blur( 5px );
	-webkit-backdrop-filter: blur( 5px );
	transition: all .5s;
}

.circle {
	width: 150px;
	height: 150px;
	background: linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(64,76,93,1) 100%, rgba(0,212,255,1) 100%);
	border-radius: 50%;
	position: absolute;
	animation: move-up6 2s ease-in infinite alternate-reverse;
}

.circle:nth-child(1) {
	top: -40px;
	left: -40px;
}

.circle:nth-child(2) {
	bottom: -40px;
	right: -40px;
	animation-name: move-down1;
}

@keyframes move-up6 {
	to {
		transform: translateY(-10px);
	}
}

@keyframes move-down1 {
  	to {
    	transform: translateY(10px);
  	}
}
</style>