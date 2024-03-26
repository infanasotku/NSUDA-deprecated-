<template>
	<div>
		<input type="checkbox" class="checkbox" :id="props.inputId"
			@change="() => { $emit('change', { id: props.inputId, value: !check }); check = !check }">
		<label class="toggle" :for="props.inputId" @change.stop>
			<div class="bars" id="bar1"></div>
			<div class="bars" id="bar2"></div>
			<div class="bars" id="bar3"></div>
		</label>
	</div>
</template>
<script lang="ts">
export default {
	name: 'bright-checkbox',
}
</script>
<script setup lang="ts">
import { ref } from 'vue';

const check = ref(false)
const props = defineProps({
	inputId: {
		type: String,
		required: true
	}
})
defineEmits([
	'change'
])
</script>
<style scoped>
.checkbox {
	display: none;
}

.toggle {
	position: relative;
	width: 20px;
	height: 20px;
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: center;
	gap: 4px;
	transition-duration: .5s;
}

.bars {
	width: 100%;
	height: 3px;
	background-color: rgb(161, 161, 161);
	border-radius: 2px;
}

#bar2 {
	transition-duration: .8s;
}

#bar1,
#bar3 {
	width: 70%;
}

.checkbox:checked+.toggle .bars {
	position: absolute;
	transition-duration: .5s;
}

.checkbox:checked+.toggle #bar2 {
	transform: scaleX(0);
	transition-duration: .5s;
}

.checkbox:checked+.toggle #bar1 {
	width: 100%;
	transform: rotate(45deg);
	transition-duration: .5s;
}

.checkbox:checked+.toggle #bar3 {
	width: 100%;
	transform: rotate(-45deg);
	transition-duration: .5s;
}

.checkbox:checked+.toggle {
	transition-duration: .5s;
	transform: rotate(180deg);
}
</style>