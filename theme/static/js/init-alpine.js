function data() {
  return {
    isSideMenuOpen: false,
    toggleSideMenu() {
      this.isSideMenuOpen = !this.isSideMenuOpen;
    },
    closeSideMenu() {
      this.isSideMenuOpen = false;
    },
    isNotificationsMenuOpen: false,
    toggleNotificationsMenu() {
      this.isNotificationsMenuOpen = !this.isNotificationsMenuOpen
    },
    closeNotificationsMenu() {
      this.isNotificationsMenuOpen = false;
    },
    // header setting
    isSettingOpen: false,
    toggleSettingMenu() {
      this.isSettingOpen = !this.isSettingOpen;
    },
    closeSettingMenu() {
      this.isSettingOpen = false;
    },
    // header Profile
    isProfileMenuOpen: false,
    toggleProfileMenu() {
      this.isProfileMenuOpen = !this.isProfileMenuOpen;
    },
    closeProfileMenu() {
      this.isProfileMenuOpen = false;
    },
    isGymMemberMenuOpen: false,
    toggleGymMemberMenu() {
      this.isGymMemberMenuOpen = !this.isGymMemberMenuOpen;
    },
    isSettingsMenuOpen: false,
    toggleSettingsMenu() {
      this.isSettingsMenuOpen = !this.isSettingsMenuOpen;
    },
    // futsal
    isFutsalMenuOpen: false,
    toggleFutsalMenu() {
      this.isFutsalMenuOpen = !this.isFutsalMenuOpen;
    },
    // Reports
    isReportsMenuOpen: false,
    toggleReportsMenu() {
      this.isReportsMenuOpen = !this.isReportsMenuOpen;
    },
    // Accountings
    isAccountingMenuOpen: false,
    toggleAccountingMenu() {
      this.isAccountingMenuOpen = !this.isAccountingMenuOpen;
    },
    // Items
    isItemsMenuOpen: false,
    toggleItemsMenu() {
      this.isItemsMenuOpen = !this.isItemsMenuOpen;
    },
    // Orders
    isOrdersMenuOpen: false,
    toggleOrdersMenu() {
      this.isOrdersMenuOpen = !this.isOrdersMenuOpen;
    },
    // Purchases
    isPurchasesMenuOpen: false,
    togglePurchasesMenu() {
      this.isPurchasesMenuOpen = !this.isPurchasesMenuOpen;
    },
    // Sales
    isSalesMenuOpen: false,
    toggleSalesMenu() {
      this.isSalesMenuOpen = !this.isSalesMenuOpen;
    },
    // Modal
    isModalOpen: false,
    trapCleanup: null,
    openModal() {
      this.isModalOpen = true;
      this.trapCleanup = focusTrap(document.querySelector('#modal'));
    },
    closeModal() {
      this.isModalOpen = false;
      this.trapCleanup();
    },


    // Product Modal
    isProductModalOpen: false,
    trapCleanup1: null,
    openProductModal() {
      this.isProductModalOpen = true
      this.trapCleanup1 = focusTrap(document.querySelector('#productModal'))
    },
    closeProductModal() {
      this.isProductModalOpen = false
      this.trapCleanup1()
    },

    // Inventory Sub Modal
    isSubModalOpen: false,
    trapCleanup2: null,
    openSubModal() {
      this.isSubModalOpen = true
      this.trapCleanup2 = focusTrap(document.querySelector('#SubModal'))
    },
    closeSubModal() {
      this.isSubModalOpen = false
      this.trapCleanup2()
    },

    // SMS Modal
    isSMSModalOpen: false,
    trapCleanupSMS: null,
    openSMSModal() {
      this.isSMSModalOpen = true
      this.trapCleanupSMS = focusTrap(document.querySelector('#SMSModal'))
    },
    closeSMSModal() {
      this.isSMSModalOpen = false
      this.trapCleanupSMS()
    },

    // View Bill Modal
    isViewBillModalOpen: false,
    trapCleanupViewBill: null,
    openViewBillModal() {
      this.isViewBillModalOpen = true
      this.trapCleanupViewBill = focusTrap(document.querySelector('#ViewBillModal'))
    },
    closeViewBillModal() {
      this.isViewBillModalOpen = false
      this.trapCleanupViewBill()
    },
    
  }
}
