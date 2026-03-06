<script setup lang="ts">
    import { Circle } from 'lucide-vue-next';
    import { computed } from 'vue'

    interface Props {
        label: String
        colourSelect: number
    }

    const props = defineProps<Props>();

    const iconColourClass = computed(() => {
        if (props.colourSelect === 1) return "text-slate-500";
        else if (props.colourSelect === 2) return "text-gray-300";
        return "text-lime-500";
    });

</script>

<template>
    <div class="flex flex-row gap-2 items-center">
        <Circle :size="22" :class="iconColourClass" fill="currentColor"/>
        <div class="text-gray-400 text-md font-bold font-chakra">
            {{ label }}
        </div>
    </div>
</template>