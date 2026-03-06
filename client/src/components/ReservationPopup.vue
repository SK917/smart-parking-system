<script setup lang="ts">
    import { ref } from 'vue';
    import { Copy, Check } from 'lucide-vue-next';

    interface Props {
        isOpen: boolean;
        reservationId: string;
        spotNum: number;
    }
    const props = defineProps<Props>();

    const emit = defineEmits(['confirm']);

    const copied = ref(false);

    const copyToClipboard = async () => {
        try {
            await navigator.clipboard.writeText(props.reservationId);
            copied.value = true;
            // Reset the icon back to "Copy" after 2 seconds
            setTimeout(() => {
                copied.value = false;
            }, 2000);
        } catch (err) {
            console.error('Failed to copy text: ', err);
        }
    };
</script>

<template>
    <Teleport to="body">
        <div 
            v-if="isOpen" 
            class="fixed inset-0 z-100 flex items-center justify-center bg-gray-300/40 backdrop-blur-sm"
        >
            <div class="bg-white border-2 border-lime-500 p-8 rounded-lg shadow-2xl max-w-sm w-full font-chakra">
                <h2 class="text-2xl font-bold text-lime-700 mb-4 uppercase text-center">
                    Reservation Confirmed
                </h2>
                
                <div class="space-y-4 mb-8 text-center">
                    <div>
                        <span class="text-gray-500 text-sm">You have successfully reserved Spot #</span>
                        <span class="text-gray-600 text-xl font-bold">{{ spotNum }}</span>
                        <span class="text-gray-500 text-sm">.</span>
                    </div>
                    
                    <div>
                        <p class="text-gray-500 text-sm mb-1">Your Reservation ID is:</p>
                        
                        <div class="relative flex items-center justify-center bg-gray-200 p-2 rounded min-h-11">
                            
                            <p class="text-xl text-gray-600 font-bold font-mono">
                                {{ reservationId }}
                            </p>

                            <div class="absolute right-2 flex items-center">
                                <button 
                                    @click="copyToClipboard"
                                    class="p-1 hover:bg-gray-300 rounded transition-colors cursor-pointer group relative"
                                    title="Copy to clipboard"
                                >
                                    <Check v-if="copied" :size="20" class="text-green-600" />
                                    <Copy v-else :size="20" class="text-gray-500 group-hover:text-gray-700" />
                                    
                                    <span v-if="copied" class="absolute -top-8 left-1/2 -translate-x-1/2 bg-gray-600 text-white text-[10px] py-1 px-2 rounded whitespace-nowrap">
                                        Copied!
                                    </span>
                                </button>
                            </div>
                        </div>
                    </div>

                    <div class="text-gray-500 text-xs flex flex-col gap-2">
                        <p>Please make sure to save this information. </p>
                        <p>Click <span class="text-lime-700 font-bold">CONFIRM</span> below once you have saved both your Reservation ID and Parking Spot Number.</p> 
                        <p>You will need your <b>Name</b> and <b>Reservation ID</b> to check your booking.</p>
                    </div>
                </div>

                <button
                    @click="emit('confirm')"
                    class="w-full bg-lime-300 hover:bg-lime-500 text-gray-600 text-xl font-bold py-3 rounded uppercase transition-colors cursor-pointer"
                >
                    Confirm
                </button>

                <div class="text-xs text-red-400 text-center pt-4 leading-tight">
                    <b>Failure to arrive</b> at your reserved parking spot <b>within 20 minutes</b> of making your reservation <b>forfeits your reservation</b>.
                </div>
            </div>
        </div>
    </Teleport>
</template>